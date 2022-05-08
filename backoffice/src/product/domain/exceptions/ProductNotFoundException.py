"""
 *
 * Libraries 
 *
"""

from src.shared.domain        import DomainException
from ..valueObjects.ProductId import ProductId

"""
 *
 * Class 
 *
"""

class ProductNotFoundException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __PRODUCT_NOT_FOUND = 123

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : ProductId ) -> None:
        super().__init__( 
            self.__PRODUCT_NOT_FOUND,
            'The product {} has not been found'.format( id.getValue() )
        )