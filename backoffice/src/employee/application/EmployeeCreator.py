"""
 *
 * Libraries 
 *
"""

from src.employee.domain   import EmployeeName
from src.employee.domain   import EmployeeEmail
from src.restaurant.domain import RestaurantId
from src.employee.domain   import EmployeeRepository
from src.shared.domain     import DomainEventsPublisher
from src.restaurant.domain import RestaurantRepository
from src.employee.domain   import Employee
from src.employee.domain   import EmployeeId
from src.restaurant.domain import Restaurant
from src.shared.domain     import ServerInternalErrorException
from src.restaurant.domain import RestaurantNotFoundException
from src.employee.domain   import EmployeeAlreadyCreatedException
from src.employee.domain   import EmployeeNameAlreadyCreatedException

"""
 *
 * Class
 *
"""

class EmployeeCreator:

    """
     *
     * Parameters 
     *
    """
 
    __repository           : EmployeeRepository
    __restaurantRepository : RestaurantRepository
    __eventPublisher       : DomainEventsPublisher

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository           : EmployeeRepository,
        restaurantRepository : RestaurantRepository,
        eventPublisher        : DomainEventsPublisher
    ) -> None:
        self.__repository           = repository
        self.__restaurantRepository = restaurantRepository
        self.__eventPublisher       = eventPublisher
    
    def createWaiter( 
        self, 
        id           : EmployeeId,
        email        : EmployeeEmail, 
        name         : EmployeeName,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        employee   : Employee
        restaurant : Restaurant
        # Code
        restaurant = self.__restaurantRepository.findById( restaurantId )
        if restaurant is None:
            raise RestaurantNotFoundException( restaurantId )
        employee = self.__repository.findByEmail( email )
        if employee is not None:
            raise EmployeeAlreadyCreatedException( email )
        employee = self.__repository.findByNameAndRestaurant( name, restaurant )
        if employee is not None:
            raise EmployeeNameAlreadyCreatedException( name )
        employee = Employee.createWaiter( id, email, name, restaurantId )
        if not self.__repository.save( employee ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( employee.pullEvents() )