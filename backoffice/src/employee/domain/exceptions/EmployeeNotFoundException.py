"""
 *
 * Libraries 
 *
"""

from src.shared.domain         import DomainException
from ..valueObjects.EmployeeId import EmployeeId

"""
 *
 * Classes 
 *
"""

class EmployeeNotFoundException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __EMPLOYEE_NOT_FOUND = 144

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : EmployeeId ) -> None:
        super().__init__( 
            self.__EMPLOYEE_NOT_FOUND,
            'The employee {} has not been found'.format( id.getValue() )
        )