"""
 *
 * Libraries 
 *
"""

from .DomainEventInformation import DomainEventInformation

"""
 *
 * Class
 *
"""

class DomainEventsInformation:

    """
     *
     * Attributes 
     *
    """

    __eventsInformation : list[DomainEventInformation]

    """
     *
     * Methods 
     *
    """

    def __init__( self, eventsInformation : list[DomainEventInformation] ) -> object:
        self.__eventsInformation = eventsInformation

    def getAll( self ) -> list[DomainEventInformation]:
        return self.__eventsInformation

    def findByEventName( self, name : str ) -> DomainEventInformation:
        # Variables
        result : DomainEventInformation
        # Code
        result = None
        for eventInformation in self.__eventsInformation:
            if eventInformation.getEventName() == name:
                result = eventInformation
                break
        return result