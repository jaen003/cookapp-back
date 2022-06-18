"""
 *
 * Libraries 
 *
"""

from ..valueObjects.ProductDescription import ProductDescription
from ..valueObjects.ProductId          import ProductId
from src.shared.domain                 import DomainEvent

"""
 *
 * Class
 *
"""

class ProductDescriptionChanged( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id          : ProductId
    __description : ProductDescription

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id          : ProductId          = None,
        description : ProductDescription = None,
        eventId     : str                = None,
        timestamp   : int                = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id          = id
        self.__description = description
    
    def getId( self ) -> ProductId:
        return self.__id

    def getDescription( self ) -> ProductDescription:
        return self.__description
    
    def getEventName( self ) -> str:
        return 'product.description.changed'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'          : self.__id.getValue(),
            'description' : self.__description.getValue()
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
        domainEvent = ProductDescriptionChanged(
            ProductId( data['id'] ),
            ProductDescription( data['description'] ),
            eventId,
            timestamp
        )
        return domainEvent

