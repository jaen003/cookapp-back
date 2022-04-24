"""
 *
 * Libraries 
 *
"""

from injector                         import inject
from ..events.DomainEventsInformation import DomainEventsInformation
from amqpstorm                        import Channel
from .RabbitmqEventBusConnector       import RabbitmqEventBusConnector
from .RabbitmqQueueNameFormatter      import RabbitmqQueueNameFormatter
from .RabbitmqExchangeNameFormatter   import RabbitmqExchangeNameFormatter

"""
 *
 * Class
 *
"""

class RabbitmqEventBusConfigurer:

    """
     *
     * Attributes 
     *
    """

    __eventBusConnector     : RabbitmqEventBusConnector
    __eventsInformation     : DomainEventsInformation
    __queueNameFormatter    : RabbitmqQueueNameFormatter
    __exchangeNameFormatter : RabbitmqExchangeNameFormatter

    """
     *
     * Methods 
     *
    """

    @inject
    def __init__( 
        self, 
        eventBusConnector     : RabbitmqEventBusConnector,
        eventsInformation     : DomainEventsInformation,
        queueNameFormatter    : RabbitmqQueueNameFormatter,
        exchangeNameFormatter : RabbitmqExchangeNameFormatter
    ) -> object:
        self.__eventBusConnector     = eventBusConnector
        self.__eventsInformation     = eventsInformation
        self.__queueNameFormatter    = queueNameFormatter
        self.__exchangeNameFormatter = exchangeNameFormatter

    def configure( self ) -> None:
        # Variables
        eventName              : str
        queueName              : str
        deadLetterQueueName    : str
        deadLetterExchangeName : str
        # Code
        for eventInformation in self.__eventsInformation.getAll():
            eventName = eventInformation.getEventName()
            self.__declareExchange( eventName )
            if eventInformation.isConsumedEvent():
                queueName = self.__queueNameFormatter.format( eventInformation )
                self.__declareQueue( queueName )
                self.__bindQueue( queueName, eventName )
                deadLetterQueueName = self.__queueNameFormatter.formatDeadLetter( eventInformation )
                deadLetterExchangeName = self.__exchangeNameFormatter.formatDeadLetter( eventName )
                self.__declareQueue( deadLetterQueueName )
                self.__declareExchange( deadLetterExchangeName )
                self.__bindQueue( deadLetterQueueName, deadLetterExchangeName )                        
    
    def __bindQueue( self, queueName : str, exchangeName : str ) -> None:
        # Variables
        channel : Channel
        # Code
        channel = self.__eventBusConnector.getChannel()
        channel.queue.bind(
            queue       = queueName,
            exchange    = exchangeName,
            routing_key = "#",
        )
        channel.close()
    
    def __declareExchange( self, exchangeName : str ) -> None:
        # Variables
        channel : Channel
        # Code
        channel = self.__eventBusConnector.getChannel()
        channel.exchange.declare(
            exchange      = exchangeName,
            exchange_type = 'fanout',
            durable       = True
        )
        channel.close()
    
    def __declareQueue( self, queueName : str ) -> None:
        # Variables
        channel : Channel
        # Code
        channel = self.__eventBusConnector.getChannel()
        channel.queue.declare(
            queue   = queueName,
            durable = True,       
        )
        channel.close()
