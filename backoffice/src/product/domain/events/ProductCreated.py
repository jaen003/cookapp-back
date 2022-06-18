"""
 *
 * Libraries 
 *
"""

from ..valueObjects.ProductName        import ProductName
from ..valueObjects.ProductPrice       import ProductPrice
from ..valueObjects.ProductDescription import ProductDescription
from ..valueObjects.ProductId          import ProductId
from src.restaurant.domain             import RestaurantId
from src.shared.domain                 import DomainEvent

"""
 *
 * Class
 *
"""

class ProductCreated( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id           : ProductId
    __name         : ProductName
    __price        : ProductPrice
    __description  : ProductDescription
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : ProductId          = None, 
        name         : ProductName        = None,
        price        : ProductPrice       = None,
        description  : ProductDescription = None,
        restaurantId : RestaurantId       = None,
        eventId      : str                = None,
        timestamp    : int                = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id           = id
        self.__name         = name
        self.__price        = price
        self.__description  = description
        self.__restaurantId = restaurantId
    
    def getId( self ) -> ProductId:
        return self.__id
    
    def getName( self ) -> ProductName:
        return self.__name
    
    def getPrice( self ) -> ProductPrice:
        return self.__price

    def getDescription( self ) -> ProductDescription:
        return self.__description
    
    def getRestaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    def getEventName( self ) -> str:
        return 'product.created'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'           : self.__id.getValue(),
            'name'         : self.__name.getValue(),
            'price'        : self.__price.getValue(),
            'description'  : self.__description.getValue(),
            'restaurantId' : self.__restaurantId.getValue()
        }
        return data

    def fromPrimitives( self, 
        eventId   : str, 
        timestamp : int, 
        data      : dict[str, str | int]
    ) -> object:
        # Variables
        domainEvent : object
        # Code
        domainEvent = ProductCreated(
            ProductId( data['id'] ),
            ProductName( data['name'] ),
            ProductPrice( data['price'] ),
            ProductDescription( data['description'] ),
            RestaurantId( data['restaurantId'] ),
            eventId,
            timestamp
        )
        return domainEvent

