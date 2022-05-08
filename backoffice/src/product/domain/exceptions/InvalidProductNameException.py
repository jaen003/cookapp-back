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

class InvalidProductNameException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_PRODUCT_NAME = 124

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : str ) -> None:
        super().__init__( 
            self.__INVALID_PRODUCT_NAME,
            'The product name {} is invalid'.format( name )
        )