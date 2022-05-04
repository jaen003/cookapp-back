"""
 *
 * Libraries 
 *
"""

from abc                             import abstractmethod
from .DiningTable                    import DiningTable
from .valueObjects.DiningTableNumber import DiningTableNumber
from .valueObjects.DiningTableId     import DiningTableId
from src.restaurant.domain           import RestaurantId

"""
 *
 * Interface
 *
"""

class DiningTableRepository:

    """
     *
     * Methods 
     *
    """
    
    @abstractmethod
    def save( self, diningTable : DiningTable ) -> bool:
        pass

    @abstractmethod
    def update( self, diningTable : DiningTable ) -> bool:
        pass

    @abstractmethod
    def findByNumberAndRestaurant( self, number : DiningTableNumber, restaurantId : RestaurantId ) -> DiningTable:
        pass

    @abstractmethod
    def findByIdAndRestaurant( self, id : DiningTableId, restaurantId : RestaurantId ) -> DiningTable:
        pass