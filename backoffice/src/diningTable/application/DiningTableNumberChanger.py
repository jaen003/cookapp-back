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
from src.diningTable.domain import DiningTableNumber
from src.shared.domain      import ServerInternalErrorException
from src.diningTable.domain import DiningTableNotFoundException
from src.diningTable.domain import DiningTableNumberAlreadyCreatedException

"""
 *
 * Class
 *
"""

class DiningTableNumberChanger:

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
    
    def change(
        self, 
        id           : DiningTableId,
        number       : DiningTableNumber,
        restaurantId : RestaurantId
    ) -> None:
        # Variables
        diningTable : DiningTable
        # Code
        diningTable = self.__repository.findByNumberAndRestaurant( number, restaurantId )
        if diningTable is not None:
            raise DiningTableNumberAlreadyCreatedException( number )
        diningTable = self.__repository.findByIdAndRestaurant( id, restaurantId )
        if diningTable is None:
            raise DiningTableNotFoundException( id )
        diningTable.renumber( number )
        if not self.__repository.update( diningTable ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( diningTable.pullEvents() )