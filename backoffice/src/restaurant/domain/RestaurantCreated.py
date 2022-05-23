"""
 *
 * Libraries 
 *
"""

from .valueObjects.RestaurantId   import RestaurantId
from .valueObjects.RestaurantName import RestaurantName
from src.shared.domain            import DomainEvent

"""
 *
 * Class
 *
"""

class RestaurantCreated( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id   : RestaurantId
    __name : RestaurantName

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : RestaurantId   = None, 
        name      : RestaurantName = None,
        eventId   : str            = None,
        timestamp : int            = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id   = id
        self.__name = name
    
    def getId( self ) -> RestaurantId:
        return self.__id
    
    def getName( self ) -> RestaurantName:
        return self.__name
    
    def getEventName( self ) -> str:
        return 'restaurant.created'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'   : self.__id.getValue(),
            'name' : self.__name.getValue(),
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
        domainEvent = RestaurantCreated(
            id        = RestaurantId( data['id'] ),
            name      = RestaurantName( data['name'] ),
            eventId   = eventId,
            timestamp = timestamp
        )
        return domainEvent

