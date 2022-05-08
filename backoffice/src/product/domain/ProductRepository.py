"""
 *
 * Libraries 
 *
"""

from abc                       import abstractmethod
from abc                       import ABCMeta
from .Product                  import Product
from .valueObjects.ProductName import ProductName
from .valueObjects.ProductId   import ProductId
from src.restaurant.domain     import RestaurantId

"""
 *
 * Interface
 *
"""

class ProductRepository( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def save( self, product : Product ) -> bool:
        pass
    
    @abstractmethod
    def update( self, product : Product ) -> bool:
        pass
    
    @abstractmethod
    def findByIdAndRestaurant( self, id : ProductId, restaurantId : RestaurantId ) -> Product:
        pass
    
    @abstractmethod
    def findByNameAndRestaurant( self, name : ProductName, restaurantId : RestaurantId ) -> Product:
        pass