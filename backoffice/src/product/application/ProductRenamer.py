"""
 *
 * Libraries 
 *
"""

from src.product.domain    import ProductName
from src.product.domain    import ProductId
from src.product.domain    import ProductRepository
from src.product.domain    import Product
from src.restaurant.domain import RestaurantId
from src.shared.domain     import ServerInternalErrorException
from src.product.domain    import ProductNameAlreadyCreatedException
from src.restaurant.domain import Restaurant
from src.shared.domain     import DomainEventsPublisher
from src.product.domain    import ProductNotFoundException

"""
 *
 * Class 
 *
"""

class ProductRenamer:

    """
     *
     * Parameters 
     *
    """
 
    __repository     : ProductRepository
    __eventPublisher : DomainEventsPublisher

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository     : ProductRepository,
        eventPublisher : DomainEventsPublisher
    ) -> None:
        self.__repository     = repository
        self.__eventPublisher = eventPublisher

    def rename( 
        self, 
        id           : ProductId, 
        name         : ProductName,
        restaurantId : RestaurantId
    ) -> None:
        # Variables
        product    : Product
        restaurant : Restaurant
        # Code
        product = self.__repository.findByNameAndRestaurant( name, restaurantId )
        if product is not None:
            raise ProductNameAlreadyCreatedException( name )
        product = self.__repository.findByIdAndRestaurant( id, restaurantId )
        if product is None:
            raise ProductNotFoundException( id )
        product.rename( name )
        if not self.__repository.update( product ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( product.pullEvents() )
