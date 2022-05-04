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

class InvalidDiningTableIdException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_DINING_TABLE_ID = 145

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : str ) -> None:
        super().__init__(
            self.__INVALID_DINING_TABLE_ID,
            'The dining table id {} is invalid'.format( id )
        )