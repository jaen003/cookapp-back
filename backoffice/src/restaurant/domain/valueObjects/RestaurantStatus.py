"""
 *
 * Libraries 
 *
"""

from src.shared.domain import IntValueObject

"""
 *
 * Class
 *
"""

class RestaurantStatus( IntValueObject ):

    """
     *
     * Constants 
     *
    """

    __ENABLED = 1

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
    
    @classmethod
    def createEnabled( cls ) -> object:
        return cls( cls.__ENABLED )