"""
 *
 * Libraries 
 *
"""

import os
from typing                                   import Any
from src.shared.domain                        import DomainEvent
from src.shared.domain                        import DomainEventSubscriber
from src.shared.domain                        import DomainException
from .DomainEventsInformation                 import DomainEventsInformation
from injector                                 import inject
from threading                                import Thread
from amqpstorm                                import Message
from amqpstorm                                import Channel
from ..eventBus.RabbitmqEventBusConnector     import RabbitmqEventBusConnector
from .JsonDomainEventDeserializer             import JsonDomainEventDeserializer
from .DomainEventInformation                  import DomainEventInformation
from ..eventBus.RabbitmqExchangeNameFormatter import RabbitmqExchangeNameFormatter
from injector                                 import Injector

"""
 *
 * Class
 *
"""

class RabbitmqDomainEventsConsumer:

    """
     *
     * Constants 
     *
    """

    __RETRY_COUNT_FIELD_NAME = 'retryCount'

    """
     *
     * Attributes 
     *
    """

    __eventBusConnector       : RabbitmqEventBusConnector
    __eventsInformation       : DomainEventsInformation
    __domainEventDeserializer : JsonDomainEventDeserializer
    __exchangeNameFormatter   : RabbitmqExchangeNameFormatter
    __messageDeliveryMode     : int
    __maximumNumberOfRetries  : int
    __injector                : Injector

    """
     *
     * Methods 
     *
    """

    @inject
    def __init__( 
        self, 
        eventBusConnector       : RabbitmqEventBusConnector,
        eventsInformation       : DomainEventsInformation,
        domainEventDeserializer : JsonDomainEventDeserializer,
        exchangeNameFormatter   : RabbitmqExchangeNameFormatter,
        injector                : Injector
    ) -> object:
        self.__eventBusConnector       = eventBusConnector
        self.__eventsInformation       = eventsInformation
        self.__domainEventDeserializer = domainEventDeserializer
        self.__exchangeNameFormatter   = exchangeNameFormatter
        self.__messageDeliveryMode     = int( os.getenv( 'EVENT_BUS_MESSAGE_DELIVERY_MODE' ) )
        self.__maximumNumberOfRetries  = int( os.getenv( 'MAXIMUM_NUMBER_OF_EVENT_BUS_RETRIES' ) )
        self.__injector                = injector

    def consume( self ) -> None:
        for eventInformation in self.__eventsInformation.getAll():  
            if eventInformation.isConsumedEvent():          
                Thread( target = self.__consumeEvent, args = ( eventInformation, ) ).start()

    def __consumeEvent( self, eventInformation : DomainEventInformation ) -> None:
        # Variables
        channel   : Channel
        queueName : str
        # Code
        channel   = self.__eventBusConnector.getChannel()
        queueName = eventInformation.formatRabbitmqQueueName()
        channel.basic.consume( 
            queue    = queueName,
            callback = lambda message:
                self.__callback( message, eventInformation )
        )
        channel.start_consuming()
    
    def __callback( 
        self, 
        message          : Message, 
        eventInformation : DomainEventInformation 
    ) -> None:
        # Variables
        domainEvent     : DomainEvent
        eventSubscriber : DomainEventSubscriber
        # Code
        domainEvent = self.__domainEventDeserializer.deserialize( message.body )
        try:
            for subscriberClass in eventInformation.getSubscriberClasses():
                eventSubscriber = self.__injector.get( subscriberClass )
                eventSubscriber.handleEvent( domainEvent )
        except DomainException:
            self.__handleConsumptionError( message, domainEvent )
        message.ack()
    
    def __handleConsumptionError( self, message : Message, domainEvent : DomainEvent ) -> None:
        # Variables
        eventName : str
        # Code
        eventName = domainEvent.getEventName()
        if self.__hasBeenRetriedTooMuch( message ):
            self.__sentToDeatLetter( message, eventName )
        else:
            self.__sendToRetry( message, eventName )

    def __hasBeenRetriedTooMuch( self, message : Message ) -> bool:
        # Variables
        retryCount : int
        # Code
        retryCount = self.__getRetryCount( message )
        return retryCount >= ( self.__maximumNumberOfRetries - 1 )
    
    def __getRetryCount( self, message : Message ) -> int:
        # Variables
        messageHeaders : dict[str, str | int]
        retryCount     : int
        # Code
        messageHeaders = message.properties['headers']
        retryCount     = 0
        if messageHeaders:
            retryCount = messageHeaders[self.__RETRY_COUNT_FIELD_NAME]
        return retryCount

    def __sendToRetry( self, message : Message, eventName : str ) -> None:
        # Variables
        retryCount        : int
        messageBody       : str
        messageProperties : dict[str, Any]
        # Code
        retryCount = self.__getRetryCount( message )
        messageProperties = {
            'delivery_mode' : self.__messageDeliveryMode,
            'headers'       : { self.__RETRY_COUNT_FIELD_NAME : ( retryCount + 1 ) }
        }
        messageBody = message.body
        self.__sendMessage( eventName, messageBody, messageProperties )
    
    def __sentToDeatLetter( self, message : Message, eventName : str ) -> None:
        # Variables
        exchangeName : str
        messageBody  : str
        # Code
        messageBody  = message.body
        exchangeName = self.__exchangeNameFormatter.formatDeadLetter( eventName )
        self.__sendMessage( exchangeName, messageBody )

    def __sendMessage( 
        self,
        exchangeName : str,
        body         : str,
        properties   : dict[str, Any] = {}
    ) -> None:
        # Variables
        channel : Channel    
        # Code                
        if not properties:
            properties = { 'delivery_mode' : self.__messageDeliveryMode }
        channel = self.__eventBusConnector.getChannel()        
        channel.basic.publish( 
            exchange    = exchangeName,
            routing_key = '',
            body        = body,
            properties  = properties
        )
        channel.close()