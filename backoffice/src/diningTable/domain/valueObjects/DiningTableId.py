"""
 *
 * Libraries 
 *
"""

from src.shared.domain                          import UuidValueObject
from ..exceptions.InvalidDiningTableIdException import InvalidDiningTableIdException

"""
 *
 * Class
 *
"""

class DiningTableId( UuidValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidDiningTableIdException( value )
