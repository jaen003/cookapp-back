"""
 *
 * Libraries 
 *
"""

from ..valueObjects.ProductPrice import ProductPrice
from ..valueObjects.ProductId    import ProductId
from src.shared.domain           import DomainEvent

"""
 *
 * Class
 *
"""

class ProductPriceChanged( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id    : ProductId
    __price : ProductPrice

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : ProductId    = None,
        price     : ProductPrice = None,
        eventId   : str          = None,
        timestamp : int          = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id    = id
        self.__price = price
    
    def getId( self ) -> ProductId:
        return self.__id
    
    def getPrice( self ) -> ProductPrice:
        return self.__price
    
    def getEventName( self ) -> str:
        return 'product.price.changed'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'    : self.__id.getValue(),
            'price' : self.__price.getValue()
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
        domainEvent = ProductPriceChanged(
            id        = ProductId( data['id'] ),
            price     = ProductPrice( data['price'] ),
            eventId   = eventId,
            timestamp = timestamp
        )
        return domainEvent

