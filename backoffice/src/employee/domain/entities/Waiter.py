"""
 *
 * Libraries 
 *
"""

from .Employee                     import Employee
from ..valueObjects.EmployeeName   import EmployeeName
from ..valueObjects.EmployeeEmail  import EmployeeEmail
from ..valueObjects.EmployeeId     import EmployeeId
from src.restaurant.domain         import RestaurantId
from ..valueObjects.EmployeeStatus import EmployeeStatus
from ..valueObjects.EmployeeRole   import EmployeeRole
from ..events.EmployeeCreated      import EmployeeCreated

"""
 *
 * Class
 *
"""

class Waiter( Employee ):

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
        super().__init__(
            id           = id,
            email        = email,
            name         = name,
            role         = role,
            status       = status,
            restaurantId = restaurantId,
        )

    @classmethod
    def create(
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