"""
 *
 * Libraries 
 *
"""

from abc                         import abstractmethod
from .entities.Employee          import Employee
from .valueObjects.EmployeeEmail import EmployeeEmail
from src.restaurant.domain       import RestaurantId
from .valueObjects.EmployeeName  import EmployeeName
from .valueObjects.EmployeeId    import EmployeeId

"""
 *
 * Interface
 *
"""

class EmployeeRepository:

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def save( self, employee : Employee ) -> bool:
        pass

    @abstractmethod
    def update( self, employee : Employee ) -> bool:
        pass

    @abstractmethod
    def findByNameAndRestaurant( self, name : EmployeeName, restaurantId : RestaurantId ) -> Employee:
        pass
    
    @abstractmethod
    def findByIdAndRestaurant( self, id : EmployeeId, restaurantId : RestaurantId ) -> Employee:
        pass
    
    @abstractmethod
    def findByEmail( self, email : EmployeeEmail ) -> Employee:
        pass