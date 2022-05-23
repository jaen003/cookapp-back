"""
 *
 * Libraries 
 *
"""

from src.restaurant.domain import RestaurantCreated
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import Restaurant
from src.shared.domain     import DomainEventSubscriber
from src.shared.domain     import ServerInternalErrorException
from injector              import inject

"""
 *
 * Class 
 *
"""

class RestaurantCreator( DomainEventSubscriber[RestaurantCreated] ):

    """
     *
     * Attributes 
     *
    """
 
    __repository : RestaurantRepository

    """
     *
     * Methods 
     *
    """

    @inject
    def __init__( self, repository : RestaurantRepository ) -> None:
        self.__repository = repository
    
    def handleEvent( self, domainEvent : RestaurantCreated ) -> None:
        # Variables
        restaurant : Restaurant
        # Code
        restaurant = self.__repository.findById( domainEvent.getId() )
        if restaurant is None:
            restaurant = Restaurant.create( domainEvent.getId(), domainEvent.getName() )
            if not self.__repository.save( restaurant ):
                raise ServerInternalErrorException()
