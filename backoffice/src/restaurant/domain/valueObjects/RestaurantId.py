"""
 *
 * Libraries 
 *
"""

from src.shared.domain import UuidValueObject

"""
 *
 * Class
 *
"""

class RestaurantId( UuidValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str = None ) -> None:
        super().__init__( value )