"""
 *
 * Libraries 
 *
"""

from unittest           import TestCase
from src.product.domain import ProductDescription
from src.shared.domain  import DomainException

"""
 *
 * Class
 *
"""

class ProductDescriptionTest( TestCase ):

    """
     *
     * Methods
     *
    """

    def testIsValidDescription( self ) -> None:
        # Variables
        valueObject  : ProductDescription
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = ProductDescription( 'Cheese, bacon, onion, lettuce' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testIsInvalidDescription( self ) -> None:
        # Variables
        valueObject  : ProductDescription
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = ProductDescription( '' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 125 )