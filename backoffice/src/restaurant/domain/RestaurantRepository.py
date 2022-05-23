"""
 *
 * Libraries 
 *
"""

from abc                        import abstractmethod
from .Restaurant                import Restaurant
from .valueObjects.RestaurantId import RestaurantId
from abc                        import ABCMeta

"""
 *
 * Interface
 *
"""

class RestaurantRepository( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """

    @abstractmethod
    def findById( self, id : RestaurantId ) -> Restaurant:
        pass
    
    @abstractmethod
    def save( self, restaurant : Restaurant ) -> bool:
        pass