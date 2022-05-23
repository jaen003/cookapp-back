"""
 *
 * Libraries 
 *
"""

from src.shared.domain          import DomainException
from .valueObjects.RestaurantId import RestaurantId

"""
 *
 * Class
 *
"""

class RestaurantNotFoundException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __RESTAURANT_NOT_FOUND = 110

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : RestaurantId ) -> None:
        super().__init__( 
            self.__RESTAURANT_NOT_FOUND,
            'The restaurant {} has not been found'.format( id.getValue() )
        )