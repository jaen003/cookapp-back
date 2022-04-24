"""
 *
 * Libraries 
 *
"""

from src.shared.domain                         import StringValueObject
from ..exceptions.InvalidEmployeeNameException import InvalidEmployeeNameException

"""
 *
 * Classes 
 *
"""

class EmployeeName( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str ) -> None:
        super().__init__( value )
        if self.isEmpty():
            raise InvalidEmployeeNameException( value )