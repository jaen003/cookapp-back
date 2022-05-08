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

class InvalidDiningTableNumberException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_DINING_TABLE_NUMBER = 146

    """
     *
     * Methods 
     *
    """

    def __init__( self, number : int ) -> None:
        super().__init__(
            self.__INVALID_DINING_TABLE_NUMBER,
            'The dining table number {} is invalid'.format( number )
        )