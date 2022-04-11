"""
 *
 * Libraries 
 *
"""

from .events.DomainEvent import DomainEvent

"""
 *
 * Class 
 *
"""

class AggregateRoot:

    """
     *
     * Attributes 
     *
    """

    __domainEvents : list[ DomainEvent ]

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        self.__domainEvents = []
    
    def recordEvent( self, domainEvent : DomainEvent ) -> None:
        self.__domainEvents.append( domainEvent )
    
    def pullEvents( self ) -> list[ DomainEvent ]:
        # Variables
        events : list[ DomainEvent ]
        # Code
        events = self.__domainEvents
        self.__domainEvents = []
        return events


