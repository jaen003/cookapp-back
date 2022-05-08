"""
 *
 * Libraries 
 *
"""

from src.shared.domain                        import StringValueObject
from ..exceptions.InvalidProductNameException import InvalidProductNameException

"""
 *
 * Class 
 *
"""

class ProductName( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidProductNameException( value )