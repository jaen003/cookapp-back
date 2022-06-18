"""
 *
 * Libraries 
 *
"""

from src.shared.domain            import DomainEvent
from ..valueObjects.EmployeeId    import EmployeeId
from ..valueObjects.EmployeeEmail import EmployeeEmail
from ..valueObjects.EmployeeName  import EmployeeName
from ..valueObjects.EmployeeRole  import EmployeeRole
from src.restaurant.domain        import RestaurantId

"""
 *
 * Class
 *
"""

class EmployeeCreated( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id           : EmployeeId
    __email        : EmployeeEmail
    __name         : EmployeeName
    __role         : EmployeeRole
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : EmployeeId    = None,
        email        : EmployeeEmail = None, 
        name         : EmployeeName  = None,
        role         : EmployeeRole  = None,
        restaurantId : RestaurantId  = None,
        eventId      : str           = None,
        timestamp    : int           = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id           = id
        self.__email        = email
        self.__name         = name
        self.__role         = role
        self.__restaurantId = restaurantId
    
    def getId( self ) -> EmployeeId:
        return self.__id

    def getEmail( self ) -> EmployeeEmail:
        return self.__email

    def getName( self ) -> EmployeeName:
        return self.__name
        
    def getRole( self ) -> EmployeeRole:
        return self.__role

    def getRestaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    def getEventName( self ) -> str:
        return 'employee.created'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'           : self.__id.getValue(),
            'email'        : self.__email.getValue(),
            'name'         : self.__name.getValue(),
            'role'         : self.__role.getValue(),
            'restaurantId' : self.__restaurantId.getValue()
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
        domainEvent = EmployeeCreated(
            EmployeeId( data['id'] ),
            EmployeeEmail( data['email'] ),
            EmployeeName( data['name'] ),
            EmployeeRole( data['role'] ),
            RestaurantId( data['restaurantId'] ),
            eventId,
            timestamp
        )
        return domainEvent
