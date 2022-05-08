"""
 *
 * Libraries 
 *
"""

from src.product.domain    import ProductPrice
from src.product.domain    import ProductId
from src.product.domain    import ProductRepository
from src.product.domain    import Product
from src.restaurant.domain import RestaurantId
from src.shared.domain     import ServerInternalErrorException
from src.shared.domain     import DomainEventsPublisher
from src.product.domain    import ProductNotFoundException

"""
 *
 * Class 
 *
"""

class ProductPriceChanger:

    """
     *
     * Attributes 
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

    def change( 
        self, 
        id           : ProductId, 
        price        : ProductPrice,
        restaurantId : RestaurantId
    ) -> None:
        # Variables
        product : Product
        # Code
        product = self.__repository.findByIdAndRestaurant( id, restaurantId )
        if product is None:
            raise ProductNotFoundException( id )
        product.changePrice( price )
        if not self.__repository.update( product ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( product.pullEvents() )
