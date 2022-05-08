"""
 *
 * Libraries 
 *
"""

from ..valueObjects.ProductId import ProductId
from src.shared.domain        import DomainEvent

"""
 *
 * Class
 *
"""

class ProductDeleted( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id : ProductId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : ProductId   = None,
        eventId   : str         = None,
        timestamp : int         = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id   = id
    
    def getId( self ) -> ProductId:
        return self.__id
    
    def getEventName( self ) -> str:
        return 'product.deleted'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id' : self.__id.getValue()
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
        domainEvent = ProductDeleted(
            id        = ProductId( data['id'] ),
            eventId   = eventId,
            timestamp = timestamp
        )
        return domainEvent

