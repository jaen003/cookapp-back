"""
 *
 * Libraries 
 *
"""

from src.shared.domain          import DomainException
from ..valueObjects.ProductName import ProductName

"""
 *
 * Class 
 *
"""

class ProductNameAlreadyCreatedException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __PRODUCT_NAME_ALREADY_CREATED = 162

    """
     *
     * Methods 
     *
    """

    def __init__( self, name : ProductName ) -> None:
        super().__init__( 
            self.__PRODUCT_NAME_ALREADY_CREATED,
            'The product name {} has already been created'.format( name.getValue() )
        )