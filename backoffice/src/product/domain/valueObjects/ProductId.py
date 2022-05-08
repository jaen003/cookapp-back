"""
 *
 * Libraries 
 *
"""

from src.shared.domain                      import StringValueObject
from ..exceptions.InvalidProductIdException import InvalidProductIdException

"""
 *
 * Class 
 *
"""

class ProductId( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidProductIdException( id )