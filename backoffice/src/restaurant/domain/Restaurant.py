"""
 *
 * Libraries 
 *
"""

from src.shared.domain              import AggregateRoot
from .valueObjects.RestaurantName   import RestaurantName
from .valueObjects.RestaurantId     import RestaurantId
from .valueObjects.RestaurantStatus import RestaurantStatus

"""
 *
 * Class
 *
"""

class Restaurant( AggregateRoot ):

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