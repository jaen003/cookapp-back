"""
 *
 * Libraries 
 *
"""

from unittest          import TestCase
from src.shared.domain import StringValueObject

"""
 *
 * Class
 *
"""

class StringValueObjectTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsNotAnEqualObject( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world' )
        response    = valueObject.equals( StringValueObject( 'hello world!' ) )
        self.assertFalse( response )
    
    def testIsAnEqualObject( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world!' )
        response    = valueObject.equals( StringValueObject( 'hello world!' ) )
        self.assertTrue( response )
    
    def testIsNotAnEqualObjectBecauseItIsNotAnComparableObject( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world!' )
        response    = valueObject.equals( 'hello world!' )
        self.assertFalse( response )
    
    def testIsNotAnEqualObjectBecauseItIsNotAnComparableObject2( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world!' )
        response    = valueObject.equals( None )
        self.assertFalse( response )
    
    def testIsAnEmptyObject( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( '' )
        response    = valueObject.isEmpty()
        self.assertTrue( response )
    
    def testIsNotAnEmptyObject( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world!' )
        response    = valueObject.isEmpty()
        self.assertFalse( response )
    
    def testIsAnObjectLongerThan( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world!' )
        response    = valueObject.isLongerThan( StringValueObject( 'hello world' ) )
        self.assertTrue( response )
    
    def testIsNotAnObjectLongerThan( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world' )
        response    = valueObject.isLongerThan( StringValueObject( 'hello world!' ) )
        self.assertFalse( response )
    
    def testIsNotAnObjectLongerThan2( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world!' )
        response    = valueObject.isLongerThan( StringValueObject( 'hello world!' ) )
        self.assertFalse( response )
    
    def testIsAnObjectLongerThanOrEqual( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world!' )
        response    = valueObject.isLongerThanOrEqual( StringValueObject( 'hello world' ) )
        self.assertTrue( response )
    
    def testIsAnObjectLongerThanOrEqual2( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world' )
        response    = valueObject.isLongerThanOrEqual( StringValueObject( 'hello world' ) )
        self.assertTrue( response )
    
    def testIsNotAnObjectLongerThanOrEqual( self ) -> None:
        # Variables
        valueObject : StringValueObject
        response    : bool
        # Code
        valueObject = StringValueObject( 'hello world' )
        response    = valueObject.isLongerThanOrEqual( StringValueObject( 'hello world!' ) )
        self.assertFalse( response )