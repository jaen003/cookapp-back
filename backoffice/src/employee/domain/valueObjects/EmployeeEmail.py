"""
 *
 * Libraries 
 *
"""

from src.shared.domain                          import StringValueObject
from ..exceptions.InvalidEmployeeEmailException import InvalidEmployeeEmailException

"""
 *
 * Class
 *
"""

class EmployeeEmail( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidEmployeeEmailException( value )