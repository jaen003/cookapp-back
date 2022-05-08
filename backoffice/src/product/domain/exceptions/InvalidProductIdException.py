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

class InvalidProductIdException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_PRODUCT_ID = 109

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : str ) -> None:
        super().__init__( 
            self.__INVALID_PRODUCT_ID,
            'The product id {} is invalid'.format( id )
        )