"""
 *
 * Libraries 
 *
"""

from src.diningTable.domain import DiningTableId
from src.diningTable.domain import DiningTableNumber
from src.diningTable.domain import DiningTableDescription
from src.diningTable.domain import DiningTable
from src.restaurant.domain  import RestaurantId
from src.diningTable.domain import DiningTableRepository
from src.shared.domain      import DomainEventsPublisher
from src.restaurant.domain  import RestaurantRepository
from src.restaurant.domain  import Restaurant
from src.shared.domain      import ServerInternalErrorException
from src.restaurant.domain  import RestaurantNotFoundException
from src.diningTable.domain import DiningTableNumberAlreadyCreatedException

"""
 *
 * Class
 *
"""

class DiningTableCreator:

    """
     *
     * Attributes 
     *
    """
 
    __repository           : DiningTableRepository
    __restaurantRepository : RestaurantRepository
    __eventPublisher       : DomainEventsPublisher

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository           : DiningTableRepository,
        restaurantRepository : RestaurantRepository,
        eventPublisher       : DomainEventsPublisher
    ) -> None:
        self.__repository           = repository
        self.__restaurantRepository = restaurantRepository
        self.__eventPublisher       = eventPublisher
    
    def create( 
        self, 
        id           : DiningTableId,
        number       : DiningTableNumber, 
        description  : DiningTableDescription,
        restaurantId : RestaurantId
    ) -> None:
        # Variables
        diningTable : DiningTable
        restaurant  : Restaurant
        # Code
        restaurant = self.__restaurantRepository.findById( restaurantId )
        if restaurant is None:
            raise RestaurantNotFoundException( restaurantId )
        diningTable = self.__repository.findByNumberAndRestaurant( number, restaurantId )
        if diningTable is not None:
            raise DiningTableNumberAlreadyCreatedException( number )
        diningTable = DiningTable.create( id, number, description, restaurantId )
        if not self.__repository.save( diningTable ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( diningTable.pullEvents() )