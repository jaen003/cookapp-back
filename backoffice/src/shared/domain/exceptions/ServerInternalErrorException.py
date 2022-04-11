"""
 *
 * Libraries 
 *
"""

from .DomainException import DomainException

"""
 *
 * Class 
 *
"""

class ServerInternalErrorException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __SERVER_INTERNAL_ERROR = 103

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        super().__init__( 
            self.__SERVER_INTERNAL_ERROR,
            'Internal server error occurred while the request was being processed'
        )
