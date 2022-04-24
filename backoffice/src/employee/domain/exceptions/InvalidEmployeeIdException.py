"""
 *
 * Libraries 
 *
"""

from src.shared.domain import DomainException

"""
 *
 * Classes 
 *
"""

class InvalidEmployeeIdException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_EMPLOYEE_ID = 143

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : str ) -> None:
        super().__init__(
            self.__INVALID_EMPLOYEE_ID,
            'The employee id {} is invalid'.format( id )
        )