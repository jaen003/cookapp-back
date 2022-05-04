"""
 *
 * Libraries 
 *
"""

from src.restaurant.domain  import RestaurantId
from src.diningTable.domain import DiningTableRepository
from src.shared.domain      import DomainEventsPublisher
from src.diningTable.domain import DiningTable
from src.diningTable.domain import DiningTableId
from src.shared.domain      import ServerInternalErrorException
from src.employee.domain    import EmployeeNotFoundException

"""
 *
 * Class
 *
"""

class DiningTableDeletor:

    """
     *
     * Parameters 
     *
    """
 
    __repository     : DiningTableRepository
    __eventPublisher : DomainEventsPublisher

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository     : DiningTableRepository,
        eventPublisher : DomainEventsPublisher
    ) -> None:
        self.__repository     = repository
        self.__eventPublisher = eventPublisher
    
    def delete(
        self, 
        id           : DiningTableId,
        restaurantId : RestaurantId
    ) -> None:
        # Variables
        diningTable : DiningTable
        # Code
        diningTable = self.__repository.findByIdAndRestaurant( id, restaurantId )
        if diningTable is None:
            raise EmployeeNotFoundException( id )
        diningTable.delete()
        if not self.__repository.update( diningTable ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( diningTable.pullEvents() )