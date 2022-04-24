"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainEvent

"""
 *
 * Class
 *
"""

class DomainEventInformation:

    """
     *
     * Attributes 
     *
    """

    __eventClass        : type
    __subscriberClasses : list[type]

    """
     *
     * Methods 
     *
    """

    def __init__( self, eventClass : type, subscriberClasses : list[type] ) -> object:
        self.__eventClass        = eventClass
        self.__subscriberClasses = subscriberClasses
    
    def getSubscriberClasses( self ) -> list[type]:
        return self.__subscriberClasses

    def getEventClass( self ) -> type:
        return self.__eventClass;

    def getEventName( self ) -> str:
        # Variables
        domainEvent : DomainEvent
        # Code
        domainEvent = self.__eventClass()
        return domainEvent.getEventName()

    def formatRabbitmqQueueName( self ) -> str:
        return 'backoffice.{}'.format( self.getEventName() );
    
    def isConsumedEvent( self ) -> bool:
        return len( self.__subscriberClasses ) > 0
    



