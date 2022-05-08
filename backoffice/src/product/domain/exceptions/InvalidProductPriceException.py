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

class InvalidProductPriceException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __INVALID_PRODUCT_PRICE = 126

    """
     *
     * Methods 
     *
    """

    def __init__( self, price : int ) -> None:
        super().__init__( 
            self.__INVALID_PRODUCT_PRICE,
            'The product price {} is invalid'.format( price )
        )