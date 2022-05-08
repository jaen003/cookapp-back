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

class InvalidProductDescriptionException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_PRODUCT_DESCRIPTION = 125

    """
     *
     * Methods 
     *
    """

    def __init__( self, description : str ) -> None:
        super().__init__( 
            self.__INVALID_PRODUCT_DESCRIPTION,
            'The product description {} is invalid'.format( description )
        )