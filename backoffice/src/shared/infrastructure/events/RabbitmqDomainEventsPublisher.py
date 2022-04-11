"""
 *
 * Libraries 
 *
"""

import os
from src.shared.domain                    import DomainEvent
from src.shared.domain                    import DomainEventsPublisher
from injector                             import inject
from .JsonDomainEventSerializer           import JsonDomainEventSerializer
from amqpstorm                            import Channel
from ..eventBus.RabbitmqEventBusConnector import RabbitmqEventBusConnector
from typing                               import Any
from threading                            import Thread

"""
 *
 * Class
 *
"""

class RabbitmqDomainEventsPublisher( DomainEventsPublisher ):

    """
     *
     * Attributes 
     *
    """

    __eventBusConnector   : RabbitmqEventBusConnector
    __messageDeliveryMode : int

    """
     *
     * Methods 
     *
    """

    @inject
    def __init__( self, eventBusConnector : RabbitmqEventBusConnector ) -> object:
        self.__eventBusConnector   = eventBusConnector
        self.__messageDeliveryMode = int( os.getenv( 'EVENT_BUS_MESSAGE_DELIVERY_MODE' ) )

    def publish( self, domainEvents : list[DomainEvent] ) -> None:        
        for domainEvent in domainEvents:            
            Thread( target = self.__publishEvent, args = ( domainEvent, ) ).start()
    
    def __publishEvent( self, domainEvent : DomainEvent ) -> None:
        # Variables
        messageBody : str
        eventName   : str
        # Code
        messageBody = JsonDomainEventSerializer.serialize( domainEvent )
        eventName   = domainEvent.getEventName()
        self.__sendMessage( eventName, messageBody )
        
    def __sendMessage( self, exchangeName : str, body : str ) -> None:
        # Variables
        channel    : Channel
        properties : dict[str, Any]
        # Code
        channel    = self.__eventBusConnector.getChannel()
        properties = { 'delivery_mode' : self.__messageDeliveryMode }
        channel.basic.publish( 
            exchange    = exchangeName,
            routing_key = '',
            body        = body,
            properties  = properties
        )
        channel.close()