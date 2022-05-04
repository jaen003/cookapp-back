"""
 *
 * Libraries 
 *
"""

from unittest               import TestCase
from src.diningTable.domain import DiningTableId
from src.shared.domain      import DomainException

"""
 *
 * Class
 *
"""

class DiningTableIdTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsValidId( self ) -> None:
        # Variables
        valueObject  : DiningTableId
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = DiningTableId( '71ef47b0-baa2-47c5-ac3c-e56036a5709e' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testIsInValidId( self ) -> None:
        # Variables
        valueObject  : DiningTableId
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = DiningTableId( '' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 145 )