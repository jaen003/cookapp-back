"""
 *
 * Libraries 
 *
"""

from unittest          import TestCase
from src.shared.domain import UuidValueObject

"""
 *
 * Class
 *
"""

class UuidValueObjectTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsNotAnEqualObject( self ) -> None:
        # Variables
        valueObject : UuidValueObject
        response    : bool
        # Code
        valueObject = UuidValueObject( '56de485d-304e-41a3-b822-d129e464a1ea' )
        response    = valueObject.equals( UuidValueObject( '56de485d-304e-41a3-b822-d129e464a1ee' ) )
        self.assertFalse( response )
    
    def testIsAnEqualObject( self ) -> None:
        # Variables
        valueObject : UuidValueObject
        response    : bool
        # Code
        valueObject = UuidValueObject( '56de485d-304e-41a3-b822-d129e464a1ea' )
        response    = valueObject.equals( UuidValueObject( '56de485d-304e-41a3-b822-d129e464a1ea' ) )
        self.assertTrue( response )
    
    def testIsNotAnEqualObjectBecauseItIsNotAnComparableObject( self ) -> None:
        # Variables
        valueObject : UuidValueObject
        response    : bool
        # Code
        valueObject = UuidValueObject( '56de485d-304e-41a3-b822-d129e464a1ea' )
        response    = valueObject.equals( '56de485d-304e-41a3-b822-d129e464a1ea' )
        self.assertFalse( response )
    
    def testIsNotAnEqualObjectBecauseItIsNotAnComparableObject2( self ) -> None:
        # Variables
        valueObject : UuidValueObject
        response    : bool
        # Code
        valueObject = UuidValueObject( '56de485d-304e-41a3-b822-d129e464a1ea' )
        response    = valueObject.equals( None )
        self.assertFalse( response )
    
    def testIsAnEmptyObject( self ) -> None:
        # Variables
        valueObject : UuidValueObject
        response    : bool
        # Code
        valueObject = UuidValueObject( '' )
        response    = valueObject.isEmpty()
        self.assertTrue( response )
    
    def testIsNotAnEmptyObject( self ) -> None:
        # Variables
        valueObject : UuidValueObject
        response    : bool
        # Code
        valueObject = UuidValueObject( '56de485d-304e-41a3-b822-d129e464a1ea' )
        response    = valueObject.isEmpty()
        self.assertFalse( response )
    
    def testIsAGeneratedValue( self ) -> None:
        # Variables
        valueObject : UuidValueObject
        value       : str
        # Code
        valueObject = UuidValueObject()
        value       = valueObject.getValue()
        self.assertNotEqual( value, '' )