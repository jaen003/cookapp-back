"""
 *
 * Libraries 
 *
"""

from unittest           import TestCase
from src.product.domain import ProductStatus

"""
 *
 * Class
 *
"""

class ProductStatusTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsEnabled( self ) -> None:
        # Variables
        valueObject : ProductStatus
        # Code
        valueObject = ProductStatus.createEnabled()
        self.assertEqual( valueObject.getValue(), 1 )
    
    def testIsDeleted( self ) -> None:
        # Variables
        valueObject : ProductStatus
        # Code
        valueObject = ProductStatus.createDeleted()
        self.assertEqual( valueObject.getValue(), 2 )