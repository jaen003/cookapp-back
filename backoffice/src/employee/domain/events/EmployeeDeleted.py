"""
 *
 * Libraries 
 *
"""

from src.shared.domain         import DomainEvent
from ..valueObjects.EmployeeId import EmployeeId

"""
 *
 * Class
 *
"""

class EmployeeDeleted( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id : EmployeeId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : EmployeeId = None,
        eventId   : str        = None,
        timestamp : int        = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id = id
    
    def getId( self ) -> EmployeeId:
        return self.__id
    
    def getEventName( self ) -> str:
        return 'employee.deleted'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id' : self.__id.getValue()
        }
        return data

    def fromPrimitives( self, 
        eventId   : str, 
        timestamp : int, 
        data      : dict[str, str | int]
    ) -> object:
        # Variables
        domainEvent : object
        # Code
        domainEvent = EmployeeDeleted(
            id        = EmployeeId( data['id'] ),
            eventId   = eventId,
            timestamp = timestamp
        )
        return domainEvent
