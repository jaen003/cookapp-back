"""
 *
 * Libraries 
 *
"""

from src.shared.domain           import DomainEvent
from ..valueObjects.EmployeeId   import EmployeeId
from ..valueObjects.EmployeeRole import EmployeeRole

"""
 *
 * Class
 *
"""

class EmployeeRoleChanged( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id   : EmployeeId
    __role : EmployeeRole

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : EmployeeId   = None,
        role      : EmployeeRole = None,
        eventId   : str          = None,
        timestamp : int          = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id   = id
        self.__role = role
    
    def getId( self ) -> EmployeeId:
        return self.__id
        
    def getRole( self ) -> EmployeeRole:
        return self.__role
    
    def getEventName( self ) -> str:
        return 'employee.role.changed'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'   : self.__id.getValue(),
            'role' : self.__role.getValue()
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
        domainEvent = EmployeeRoleChanged(
            EmployeeId( data['id'] ),
            EmployeeRole( data['role'] ),
            eventId,
            timestamp
        )
        return domainEvent
