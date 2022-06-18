"""
 *
 * Libraries 
 *
"""

from .valueObjects.RestaurantName   import RestaurantName
from .valueObjects.RestaurantId     import RestaurantId
from .valueObjects.RestaurantStatus import RestaurantStatus

"""
 *
 * Class
 *
"""

class Restaurant:

    """
     *
     * Attributes 
     *
    """

    __id     : RestaurantId
    __name   : RestaurantName
    __status : RestaurantStatus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id     : RestaurantId,
        name   : RestaurantName,
        status : RestaurantStatus,
    ) -> None:
        self.__id     = id
        self.__name   = name
        self.__status = status
    
    def getId( self ) -> RestaurantId:
        return self.__id

    def getName( self ) -> RestaurantName:
        return self.__name
    
    def getStatus( self ) -> RestaurantStatus:
        return self.__status
    
    @classmethod
    def create( cls, id : RestaurantId, name : RestaurantName ) -> object:
        return cls( id, name, RestaurantStatus.createEnabled() )