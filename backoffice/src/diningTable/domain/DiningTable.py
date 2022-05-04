"""
 *
 * Libraries 
 *
"""

from .valueObjects.DiningTableNumber      import DiningTableNumber
from .valueObjects.DiningTableDescription import DiningTableDescription
from .valueObjects.DiningTableId          import DiningTableId
from src.restaurant.domain                import RestaurantId
from .valueObjects.DiningTableStatus      import DiningTableStatus
from src.shared.domain                    import AggregateRoot
from .events.DiningTableCreated           import DiningTableCreated

"""
 *
 * Class
 *
"""

class DiningTable( AggregateRoot ):

    """
     *
     * Attributes 
     *
    """

    __id           : DiningTableId
    __number       : DiningTableNumber
    __description  : DiningTableDescription
    __status       : DiningTableStatus
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self,
        id           : DiningTableId,
        number       : DiningTableNumber,
        description  : DiningTableDescription,
        status       : DiningTableStatus,
        restaurantId : RestaurantId
    ) -> None:
        super().__init__()
        self.__id           = id
        self.__number       = number
        self.__description  = description
        self.__status       = status
        self.__restaurantId = restaurantId
    
    def getId( self ) -> DiningTableId:
        return self.__id
    
    def getNumber( self ) -> DiningTableNumber:
        return self.__number
    
    def getDescription( self ) -> DiningTableDescription:
        return self.__description
    
    def getStatus( self ) -> DiningTableStatus:
        return self.__status

    def getRestaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    @classmethod
    def create(
        cls,
        id           : DiningTableId,
        number       : DiningTableNumber,
        description  : DiningTableDescription,
        restaurantId : RestaurantId
    ) -> object:
        self = cls(
            id           = id,
            number       = number,
            description  = description,
            status       = DiningTableStatus.createEnabled(),
            restaurantId = restaurantId
        )
        self.recordEvent( DiningTableCreated(
            id           = id,
            number       = number,
            description  = description,
            restaurantId = restaurantId
        ) )
        return self