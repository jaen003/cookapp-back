"""
 *
 * Libraries 
 *
"""

from unittest            import TestCase
from src.employee.domain import EmployeeRole

"""
 *
 * Class
 *
"""

class EmployeeRoleTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsChef( self ) -> None:
        # Variables
        valueObject : EmployeeRole
        # Code
        valueObject = EmployeeRole.createChef()
        self.assertEqual( valueObject.getValue(), 2 )
    
    def testIsChef2( self ) -> None:
        # Variables
        valueObject : EmployeeRole
        # Code
        valueObject = EmployeeRole.createChef()
        self.assertTrue( valueObject.isChef() )
    
    def testIsNotChef( self ) -> None:
        # Variables
        valueObject : EmployeeRole
        # Code
        valueObject = EmployeeRole.createWaiter()
        self.assertFalse( valueObject.isChef() )
    
    def testIsWaiter( self ) -> None:
        # Variables
        valueObject : EmployeeRole
        # Code
        valueObject = EmployeeRole.createWaiter()
        self.assertEqual( valueObject.getValue(), 3 )
    
    def testIsWaiter2( self ) -> None:
        # Variables
        valueObject : EmployeeRole
        # Code
        valueObject = EmployeeRole.createWaiter()
        self.assertTrue( valueObject.isWaiter() )
    
    def testIsNotWaiter( self ) -> None:
        # Variables
        valueObject : EmployeeRole
        # Code
        valueObject = EmployeeRole.createChef()
        self.assertFalse( valueObject.isWaiter() )