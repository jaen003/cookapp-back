"""
 *
 * Libraries 
 *
"""

from unittest          import TestCase
from src.shared.domain import IntValueObject

"""
 *
 * Class
 *
"""

class IntValueObjectTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsNotAnEqualObject( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.equals( IntValueObject( 4 ) )
        self.assertFalse( response )
    
    def testIsAnEqualObject( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.equals( IntValueObject( 3 ) )
        self.assertTrue( response )

    def testIsAnObjectLessThan( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isLessThan( IntValueObject( 4 ) )
        self.assertTrue( response )
    
    def testIsNotAnObjectLessThan( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isLessThan( IntValueObject( 3 ) )
        self.assertFalse( response )
    
    def testIsNotAnObjectLessThan2( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isLessThan( IntValueObject( 2 ) )
        self.assertFalse( response )
    
    def testIsAnObjectLessThanOrEqual( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isLessThanOrEqual( IntValueObject( 3 ) )
        self.assertTrue( response )

    def testIsAnObjectLessThanOrEqual2( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isLessThanOrEqual( IntValueObject( 4 ) )
        self.assertTrue( response )
    
    def testIsNotAnObjectLessThanOrEqual( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isLessThanOrEqual( IntValueObject( 2 ) )
        self.assertFalse( response )
    
    def testIsAnObjectGreaterThan( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 4 )
        response    = valueObject.isGreaterThan( IntValueObject( 3 ) )
        self.assertTrue( response )
    
    def testIsNotAnObjectGreaterThan( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isGreaterThan( IntValueObject( 3 ) )
        self.assertFalse( response )
    
    def testIsNotAnObjectGreaterThan2( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 2 )
        response    = valueObject.isGreaterThan( IntValueObject( 3 ) )
        self.assertFalse( response )
    
    def testIsAnObjectGreaterThanOrEqual( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 3 )
        response    = valueObject.isGreaterThanOrEqual( IntValueObject( 3 ) )
        self.assertTrue( response )

    def testIsAnObjectGreaterThanOrEqual2( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 4 )
        response    = valueObject.isGreaterThanOrEqual( IntValueObject( 3 ) )
        self.assertTrue( response )
    
    def testIsNotAnObjectGreaterThanOrEqual( self ) -> None:
        # Variables
        valueObject : IntValueObject
        response    : bool
        # Code
        valueObject = IntValueObject( 2 )
        response    = valueObject.isGreaterThanOrEqual( IntValueObject( 3 ) )
        self.assertFalse( response )