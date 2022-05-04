"""
 *
 * Libraries 
 *
"""

from abc                             import abstractmethod
from .DiningTable                    import DiningTable
from .valueObjects.DiningTableNumber import DiningTableNumber
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
    def findByNumberAndRestaurant( self, number : DiningTableNumber, restaurantId : RestaurantId ) -> DiningTable:
        pass