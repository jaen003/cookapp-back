"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException

"""
 *
 * Class 
 *
"""

class InvalidEmployeeEmailException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_EMPLOYEE_EMAIL = 141

    """
     *
     * Methods 
     *
    """

    def __init__( self, email : str ) -> None:
        super().__init__(
            self.__INVALID_EMPLOYEE_EMAIL,
            'The employee email {} is invalid'.format( email )
        )