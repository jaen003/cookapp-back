"""
 *
 * Libraries 
 *
"""

from unittest            import TestCase
from src.employee.domain import EmployeeEmail
from src.shared.domain   import DomainException

"""
 *
 * Class
 *
"""

class EmployeeEmailTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsValidEmail( self ) -> None:
        # Variables
        valueObject  : EmployeeEmail
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = EmployeeEmail( 'stephen.hawking@gmail.com' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 0 )
    
    def testIsInValidEmail( self ) -> None:
        # Variables
        valueObject  : EmployeeEmail
        responseCode : int
        # Code
        responseCode = 0
        try:
            valueObject = EmployeeEmail( '' )
        except DomainException as exc:
            responseCode = exc.getCode()
        self.assertEqual( responseCode, 141 )