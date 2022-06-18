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

class Chef( Employee ):

    """
     *
     * Methods 
     *
    """

    @classmethod
    def create(
        cls,
        id           : EmployeeId,
        email        : EmployeeEmail,
        name         : EmployeeName,
        restaurantId : RestaurantId,
    ) -> object:
        self = cls(
            id,
            email,
            name,
            EmployeeRole.createChef(),
            EmployeeStatus.createEnabled(),
            restaurantId
        )
        self.recordEvent( EmployeeCreated( id, email, name, self.getRole(), restaurantId ) )
        return self