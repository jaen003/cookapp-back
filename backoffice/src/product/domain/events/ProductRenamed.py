"""
 *
 * Libraries 
 *
"""

from ..valueObjects.ProductName import ProductName
from ..valueObjects.ProductId   import ProductId
from src.shared.domain          import DomainEvent

"""
 *
 * Class
 *
"""

class ProductRenamed( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id   : ProductId
    __name : ProductName

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : ProductId   = None, 
        name      : ProductName = None,
        eventId   : str         = None,
        timestamp : int         = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id   = id
        self.__name = name
    
    def getId( self ) -> ProductId:
        return self.__id
    
    def getName( self ) -> ProductName:
        return self.__name
    
    def getEventName( self ) -> str:
        return 'product.renamed'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'   : self.__id.getValue(),
            'name' : self.__name.getValue()
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
        domainEvent = ProductRenamed(
            id        = ProductId( data['id'] ),
            name      = ProductName( data['name'] ),
            eventId   = eventId,
            timestamp = timestamp
        )
        return domainEvent

