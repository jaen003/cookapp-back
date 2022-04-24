"""
 *
 * Libraries 
 *
"""

from src.shared.domain                       import UuidValueObject
from ..exceptions.InvalidEmployeeIdException import InvalidEmployeeIdException

"""
 *
 * Class
 *
"""

class EmployeeId( UuidValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidEmployeeIdException( value )
