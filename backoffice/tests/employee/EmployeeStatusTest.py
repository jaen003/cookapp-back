"""
 *
 * Libraries 
 *
"""

from unittest            import TestCase
from src.employee.domain import EmployeeStatus

"""
 *
 * Class
 *
"""

class EmployeeStatusTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsEnabled( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createEnabled()
        self.assertEqual( valueObject.getValue(), 1 )
    
    def testIsDeleted( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createDeleted()
        self.assertEqual( valueObject.getValue(), 2 )
    
    def testIsBlocked( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createBlocked()
        self.assertEqual( valueObject.getValue(), 4 )
    
    def testIsBlocked2( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createBlocked()
        self.assertTrue( valueObject.isBlocked() )
    
    def testIsNotBlocked( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createEnabled()
        self.assertFalse( valueObject.isBlocked() )
    
    def testIsNotBlocked2( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createDeleted()
        self.assertFalse( valueObject.isBlocked() )
    
    def testIsNotBlocked3( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createDisabled()
        self.assertFalse( valueObject.isBlocked() )
    
    def testIsDisabled( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createDisabled()
        self.assertEqual( valueObject.getValue(), 3 )
    
    def testIsDisabled2( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createDisabled()
        self.assertTrue( valueObject.isDisabled() )
    
    def testIsNotDisabled( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createDeleted()
        self.assertFalse( valueObject.isDisabled() )
    
    def testIsNotDisabled2( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createEnabled()
        self.assertFalse( valueObject.isDisabled() )
    
    def testIsNotDisabled3( self ) -> None:
        # Variables
        valueObject : EmployeeStatus
        # Code
        valueObject = EmployeeStatus.createBlocked()
        self.assertFalse( valueObject.isDisabled() )