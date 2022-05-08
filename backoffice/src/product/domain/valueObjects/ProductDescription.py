"""
 *
 * Libraries 
 *
"""

from src.shared.domain                               import StringValueObject
from ..exceptions.InvalidProductDescriptionException import InvalidProductDescriptionException

"""
 *
 * Class 
 *
"""

class ProductDescription( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidProductDescriptionException( value )