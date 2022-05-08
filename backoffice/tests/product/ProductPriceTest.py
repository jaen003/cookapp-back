"""
 *
 * Libraries 
 *
"""

import unittest
from src.product.domain import ProductPrice
from src.shared.domain  import DomainException

"""
 *
 * Class 
 *
"""

class ProductPriceTest( unittest.TestCase ):

    """
     *
     * Methods 
     *
    """

    def testValidPrice( self ):
        # Variables
        responseCode : int
        valueObject  : ProductPrice
        # Code
        responseCode = 0
        try:
            valueObject = ProductPrice( 3300 )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testInvalidPrice1( self ):
        # Variables
        responseCode : int
        valueObject  : ProductPrice
        # Code
        responseCode = 0
        try:
            valueObject = ProductPrice( 0 )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 126 )

    def testInvalidPrice2( self ):
        # Variables
        responseCode : int
        valueObject  : ProductPrice
        # Code
        responseCode = 0
        try:
            valueObject = ProductPrice( -1000 )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 126 )