"""
 *
 * Libraries 
 *
"""

from unittest           import TestCase
from src.product.domain import ProductName
from src.shared.domain  import DomainException

"""
 *
 * Class
 *
"""

class ProductNameTest( TestCase ):

    """
     *
     * Methods
     *
    """

    def testIsValidName( self ) -> None:
        # Variables
        valueObject  : ProductName
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = ProductName( 'Hot dog' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testIsInvalidName( self ) -> None:
        # Variables
        valueObject  : ProductName
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = ProductName( '' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 124 )