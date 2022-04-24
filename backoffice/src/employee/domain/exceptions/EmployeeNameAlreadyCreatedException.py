"""
 *
 * Libraries 
 *
"""

from src.shared.domain           import DomainException
from ..valueObjects.EmployeeName import EmployeeName

"""
 *
 * Classes 
 *
"""

class EmployeeNameAlreadyCreatedException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __EMPLOYEE_ALREADY_CREATED = 140

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : EmployeeName ) -> None:
        super().__init__( 
            self.__EMPLOYEE_ALREADY_CREATED,
            'The employee name {} has already been created'.format( name.getValue() ),
        )