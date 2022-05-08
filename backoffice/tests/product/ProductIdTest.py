"""
 *
 * Libraries 
 *
"""

from unittest           import TestCase
from src.product.domain import ProductId
from src.shared.domain  import DomainException

"""
 *
 * Class
 *
"""

class ProductIdTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsValidId( self ) -> None:
        # Variables
        valueObject  : ProductId
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = ProductId( '71ef47b0-baa2-47c5-ac3c-e56036a5709e' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testIsInValidId( self ) -> None:
        # Variables
        valueObject  : ProductId
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = ProductId( '' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 109 )