"""
 *
 * Libraries 
 *
"""

from .valueObjects.EmployeeName   import EmployeeName
from .valueObjects.EmployeeEmail  import EmployeeEmail
from .valueObjects.EmployeeId     import EmployeeId
from src.restaurant.domain        import RestaurantId
from .valueObjects.EmployeeStatus import EmployeeStatus
from .valueObjects.EmployeeRole   import EmployeeRole
from .events.EmployeeCreated      import EmployeeCreated
from src.shared.domain            import AggregateRoot 

"""
 *
 * Class
 *
"""

class Employee( AggregateRoot ):

    """
     *
     * Attributes 
     *
    """

    __id           : EmployeeId
    __email        : EmployeeEmail
    __name         : EmployeeName
    __role         : EmployeeRole
    __status       : EmployeeStatus
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self,
        id           : EmployeeId,
        email        : EmployeeEmail,
        name         : EmployeeName,
        role         : EmployeeRole,
        status       : EmployeeStatus,
        restaurantId : RestaurantId
    ) -> None:
        super().__init__()
        self.__id           = id
        self.__email        = email
        self.__name         = name
        self.__role         = role
        self.__status       = status
        self.__restaurantId = restaurantId

    @classmethod
    def createWaiter(
        cls,
        id           : EmployeeId,
        email        : EmployeeEmail,
        name         : EmployeeName,
        restaurantId : RestaurantId,
    ) -> object:
        self = cls(
            id           = id,
            email        = email,
            name         = name,
            role         = EmployeeRole.createWaiter(),
            status       = EmployeeStatus.createEnabled(),
            restaurantId = restaurantId,
        )
        self.recordEvent( EmployeeCreated(
            id           = id,
            email        = email,
            name         = name,
            role         = self.getRole(),
            restaurantId = restaurantId
        ) )
        return self
    
    def getId( self ) -> EmployeeId:
        return self.__id

    def getEmail( self ) -> EmployeeEmail:
        return self.__email

    def getName( self ) -> EmployeeName:
        return self.__name
        
    def getRole( self ) -> EmployeeRole:
        return self.__role
    
    def getStatus( self ) -> EmployeeStatus:
        return self.__status

    def getRestaurantId( self ) -> RestaurantId:
        return self.__restaurantId