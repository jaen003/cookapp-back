"""
 *
 * Libraries 
 *
"""

from .valueObjects.DiningTableNumber       import DiningTableNumber
from .valueObjects.DiningTableDescription  import DiningTableDescription
from .valueObjects.DiningTableId           import DiningTableId
from src.restaurant.domain                 import RestaurantId
from .valueObjects.DiningTableStatus       import DiningTableStatus
from src.shared.domain                     import AggregateRoot
from .events.DiningTableCreated            import DiningTableCreated
from .events.DiningTableDeleted            import DiningTableDeleted
from .events.DiningTableNumberChanged      import DiningTableNumberChanged
from .events.DiningTableDescriptionChanged import DiningTableDescriptionChanged

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
        self = cls( id, number, description, DiningTableStatus.createEnabled(), restaurantId )
        self.recordEvent( DiningTableCreated( id, number, description, restaurantId ) )
        return self
    
    def delete( self ) -> None:
        self.__status = DiningTableStatus.createDeleted()
        self.recordEvent( DiningTableDeleted( self.__id ) )
    
    def changeNumber( self, newNumber : DiningTableNumber ) -> None:
        self.__number = newNumber
        self.recordEvent( DiningTableNumberChanged( self.__id, self.__number ) )
    
    def changeDescription( self, newDescription : DiningTableDescription ) -> None:
        self.__description = newDescription
        self.recordEvent( DiningTableDescriptionChanged( self.__id, self.__description ) )