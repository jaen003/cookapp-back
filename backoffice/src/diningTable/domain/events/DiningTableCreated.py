"""
 *
 * Libraries 
 *
"""

from ..valueObjects.DiningTableNumber      import DiningTableNumber
from ..valueObjects.DiningTableDescription import DiningTableDescription
from ..valueObjects.DiningTableId          import DiningTableId
from src.restaurant.domain                 import RestaurantId
from src.shared.domain                     import DomainEvent

"""
 *
 * Class
 *
"""

class DiningTableCreated( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id           : DiningTableId
    __number       : DiningTableNumber
    __description  : DiningTableDescription
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id           : DiningTableId          = None, 
        number       : DiningTableNumber      = None,
        description  : DiningTableDescription = None,
        restaurantId : RestaurantId           = None,
        eventId      : str                    = None,
        timestamp    : int                    = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id           = id
        self.__number       = number
        self.__description  = description
        self.__restaurantId = restaurantId
    
    def getId( self ) -> DiningTableId:
        return self.__id
    
    def getNumber( self ) -> DiningTableNumber:
        return self.__number
    
    def getDescription( self ) -> DiningTableDescription:
        return self.__description

    def getRestaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    def getEventName( self ) -> str:
        return 'dining.table.created'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'           : self.__id.getValue(),
            'number'       : self.__number.getValue(),
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
        domainEvent = DiningTableCreated(
            DiningTableId( data['id'] ),
            DiningTableNumber( data['number'] ),
            DiningTableDescription( data['description'] ),
            RestaurantId( data['restaurantId'] ),
            eventId,
            timestamp
        )
        return domainEvent

