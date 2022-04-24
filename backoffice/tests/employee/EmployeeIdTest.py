"""
 *
 * Libraries 
 *
"""

from unittest            import TestCase
from src.employee.domain import EmployeeId
from src.shared.domain   import DomainException

"""
 *
 * Class
 *
"""

class EmployeeIdTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsValidId( self ) -> None:
        # Variables
        valueObject  : EmployeeId
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = EmployeeId( '71ef47b0-baa2-47c5-ac3c-e56036a5709e' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testIsInValidId( self ) -> None:
        # Variables
        valueObject  : EmployeeId
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = EmployeeId( '' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 143 )