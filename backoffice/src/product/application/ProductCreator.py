"""
 *
 * Libraries 
 *
"""

from src.product.domain    import ProductName
from src.product.domain    import ProductPrice
from src.product.domain    import ProductDescription
from src.product.domain    import ProductId
from src.product.domain    import ProductRepository
from src.product.domain    import Product
from src.restaurant.domain import RestaurantRepository
from src.restaurant.domain import RestaurantId
from src.restaurant.domain import RestaurantNotFoundException
from src.shared.domain     import ServerInternalErrorException
from src.product.domain    import ProductNameAlreadyCreatedException
from src.restaurant.domain import Restaurant
from src.shared.domain     import DomainEventsPublisher

"""
 *
 * Class 
 *
"""

class ProductCreator:

    """
     *
     * Parameters 
     *
    """
 
    __repository           : ProductRepository
    __restaurantRepository : RestaurantRepository
    __eventPublisher       : DomainEventsPublisher

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository           : ProductRepository,
        restaurantRepository : RestaurantRepository,
        eventPublisher       : DomainEventsPublisher
    ) -> None:
        self.__repository           = repository
        self.__restaurantRepository = restaurantRepository
        self.__eventPublisher       = eventPublisher

    def create( 
        self, 
        id           : ProductId, 
        name         : ProductName,
        price        : ProductPrice,
        description  : ProductDescription,
        restaurantId : RestaurantId
    ) -> None:
        # Variables
        product    : Product
        restaurant : Restaurant
        # Code
        restaurant = self.__restaurantRepository.findById( restaurantId )
        if restaurant is None:
            raise RestaurantNotFoundException( restaurantId )
        product = self.__repository.findByNameAndRestaurant( name, restaurantId )
        if product is not None:
            raise ProductNameAlreadyCreatedException( name )
        product = Product.create( id, name, price, description, restaurantId )     
        if not self.__repository.save( product ):
            raise ServerInternalErrorException()
        self.__eventPublisher.publish( product.pullEvents() )
