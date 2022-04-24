"""
 *
 * Libraries 
 *
"""

from src.shared.domain import StringValueObject

"""
 *
 * Class
 *
"""

class RestaurantName( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )