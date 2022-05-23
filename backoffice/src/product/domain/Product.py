"""
 *
 * Libraries 
 *
"""

from .valueObjects.ProductName         import ProductName
from .valueObjects.ProductPrice        import ProductPrice
from .valueObjects.ProductDescription  import ProductDescription
from .valueObjects.ProductId           import ProductId
from src.shared.domain                 import AggregateRoot
from .events.ProductCreated            import ProductCreated
from src.restaurant.domain             import RestaurantId
from .valueObjects.ProductStatus       import ProductStatus
from .events.ProductRenamed            import ProductRenamed
from .events.ProductDeleted            import ProductDeleted
from .events.ProductPriceChanged       import ProductPriceChanged
from .events.ProductDescriptionChanged import ProductDescriptionChanged

"""
 *
 * Class 
 *
"""

class Product( AggregateRoot ):

    """
     *
     * Attributes 
     *
    """

    __id           : ProductId
    __name         : ProductName
    __price        : ProductPrice
    __description  : ProductDescription
    __status       : ProductStatus
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : ProductId, 
        name         : ProductName,
        price        : ProductPrice,
        description  : ProductDescription,
        status       : ProductStatus,
        restaurantId : RestaurantId
    ) -> None:
        super().__init__()
        self.__id           = id
        self.__name         = name
        self.__price        = price
        self.__description  = description
        self.__status       = status
        self.__restaurantId = restaurantId

    def id( self ) -> ProductId:
        return self.__id
    
    def name( self ) -> ProductName:
        return self.__name

    def price( self ) -> ProductPrice:
        return self.__price
    
    def description( self ) -> ProductDescription:
        return self.__description

    def status( self ) -> ProductStatus:
        return self.__status

    def restaurantId( self ) -> RestaurantId:
        return self.__restaurantId

    @classmethod
    def create( 
        cls, 
        id           : ProductId, 
        name         : ProductName,
        price        : ProductPrice,
        description  : ProductDescription,
        restaurantId : RestaurantId
    ) -> object:
        self = cls(
            id           = id,
            name         = name,
            price        = price,
            description  = description,
            status       = ProductStatus.createEnabled(),
            restaurantId = restaurantId,
        )
        self.recordEvent( ProductCreated(
            id           = id,
            name         = name,
            price        = price,
            description  = description,
            restaurantId = restaurantId,
        ) )
        return self

    def rename( self, newName : ProductName ) -> None:
        self.__name = newName
        self.recordEvent( ProductRenamed(
            id   = self.__id,
            name = self.__name
        ) )
    
    def delete( self ) -> None:
        self.__status = ProductStatus.createDeleted()
        self.recordEvent( ProductDeleted(
            id = self.__id
        ) )
    
    def changePrice( self, newPrice : ProductPrice ) -> None:
        self.__price = newPrice
        self.recordEvent( ProductPriceChanged(
            id    = self.__id,
            price = self.__price
        ) )
    
    def changeDescription( self, newDescription : ProductDescription ) -> None:
        self.__description = newDescription
        self.recordEvent( ProductDescriptionChanged(
            id          = self.__id,
            description = self.__description,
        ) )