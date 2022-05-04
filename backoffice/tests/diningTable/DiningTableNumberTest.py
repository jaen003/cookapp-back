"""
 *
 * Libraries 
 *
"""

from unittest               import TestCase
from src.diningTable.domain import DiningTableNumber
from src.shared.domain      import DomainException

"""
 *
 * Class
 *
"""

class DiningTableNumberTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testValidDiningTableNumber( self ):
        # Variables
        responseCode : int
        valueObject  : DiningTableNumber
        # Code
        responseCode = 0
        try:
            valueObject = DiningTableNumber( 33 )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testInvalidDiningTableNumber( self ):
        # Variables
        responseCode : int
        valueObject  : DiningTableNumber
        # Code
        responseCode = 0
        try:
            valueObject = DiningTableNumber( 0 )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 146 )

    def testInvalidDiningTableNumber2( self ):
        # Variables
        responseCode : int
        valueObject  : DiningTableNumber
        # Code
        responseCode = 0
        try:
            valueObject = DiningTableNumber( 256 )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 146 )