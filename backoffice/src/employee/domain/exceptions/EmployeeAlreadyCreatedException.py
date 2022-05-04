"""
 *
 * Libraries 
 *
"""

from src.shared.domain            import DomainException
from ..valueObjects.EmployeeEmail import EmployeeEmail

"""
 *
 * Classes 
 *
"""

class EmployeeAlreadyCreatedException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __EMPLOYEE_ALREADY_CREATED = 139

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : EmployeeEmail ) -> None:
        super().__init__( 
            self.__EMPLOYEE_ALREADY_CREATED,
            'The employee {} has already been created'.format( email.getValue() )
        )