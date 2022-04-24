"""
 *
 * Libraries 
 *
"""

from src.restaurant.domain import RestaurantId
from src.employee.domain   import EmployeeRepository
from src.shared.domain     import DomainEventsPublisher
from src.employee.domain   import Waiter
from src.employee.domain   import EmployeeId
from src.shared.domain     import ServerInternalErrorException
from src.employee.domain   import EmployeeNotFoundException

"""
 *
 * Class
 *
"""

class EmployeeRoleChanger:

    """
     *
     * Parameters 
     *
    """
 
    __repository     : EmployeeRepository
    __eventPublisher : DomainEventsPublisher

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository     : EmployeeRepository,
        eventPublisher : DomainEventsPublisher
    ) -> None:
        self.__repository     = repository
        self.__eventPublisher = eventPublisher
    
    def changeToWaiter( 
        self, 
        id           : EmployeeId,
        restaurantId : RestaurantId,
    ) -> None:
        # Variables
        employee : Waiter
        # Code
        employee = self.__repository.findByIdAndRestaurant( id, restaurantId )
        if employee is None:
            raise EmployeeNotFoundException( id )
        employee.changeToWaiter()
        if not self.__repository.update( employee ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( employee.pullEvents() )