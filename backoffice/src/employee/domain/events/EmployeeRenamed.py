"""
 *
 * Libraries 
 *
"""

from src.shared.domain           import DomainEvent
from ..valueObjects.EmployeeId   import EmployeeId
from ..valueObjects.EmployeeName import EmployeeName

"""
 *
 * Class
 *
"""

class EmployeeRenamed( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id   : EmployeeId
    __name : EmployeeName

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : EmployeeId   = None,
        name      : EmployeeName = None,
        eventId   : str          = None,
        timestamp : int          = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id   = id
        self.__name = name
    
    def getId( self ) -> EmployeeId:
        return self.__id
        
    def getName( self ) -> EmployeeName:
        return self.__name
    
    def getEventName( self ) -> str:
        return 'employee.renamed'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'   : self.__id.getValue(),
            'name' : self.__name.getValue()
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
        domainEvent = EmployeeRenamed(
            EmployeeId( data['id'] ),
            EmployeeName( data['name'] ),
            eventId,
            timestamp
        )
        return domainEvent
