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

class InvalidEmployeeNameException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_EMPLOYEE_NAME = 142

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : str ) -> None:
        super().__init__(
            self.__INVALID_EMPLOYEE_NAME,
            'The employee name {} is invalid'.format( name )
        )