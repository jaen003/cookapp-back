"""
 *
 * Libraries 
 *
"""

from unittest            import TestCase
from src.employee.domain import EmployeeName
from src.shared.domain   import DomainException

"""
 *
 * Class
 *
"""

class EmployeeNameTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsValidName( self ) -> None:
        # Variables
        valueObject  : EmployeeName
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = EmployeeName( 'Stephen Hawking' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testIsInValidName( self ) -> None:
        # Variables
        valueObject  : EmployeeName
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = EmployeeName( '' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 142 )