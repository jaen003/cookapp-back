"""
 *
 * Class
 *
"""

class IntValueObject:

    """
     *
     * Attributes 
     *
    """

    __value : int

    """
     *
     * Methods 
     *
    """

    def __init__( self, value : int ) -> object:
        self.__value = value
    
    def getValue( self ) -> int:
        return self.__value
    
    def __isAnComparableObject( self, other : object ) -> bool:
        return ( other is not None and type( self ) == type( other ) )
    
    def equals( self, other : object ) -> bool:
        # Variables
        equalObjects : bool
        # Code
        equalObjects = False
        if self.__isAnComparableObject( other ):
            equalObjects = self.__value == other.getValue()
        return equalObjects
    
    def isLessThan( self, other : object ) -> bool:
        # Variables
        response : bool
        # Code
        response = False
        if self.__isAnComparableObject( other ):
            response = self.__value < other.getValue()
        return response
    
    def isGreaterThan( self, other : object ) -> bool:
        # Variables
        response : bool
        # Code
        response = False
        if self.__isAnComparableObject( other ):
            response = self.__value > other.getValue()
        return response
    
    def isLessThanOrEqual( self, other : object ) -> bool:
        # Variables
        response : bool
        # Code
        response = False
        if self.__isAnComparableObject( other ):
            response = self.__value <= other.getValue()
        return response
    
    def isGreaterThanOrEqual( self, other : object ) -> bool:
        # Variables
        response : bool
        # Code
        response = False
        if self.__isAnComparableObject( other ):
            response = self.__value >= other.getValue()
        return response
    
    def toString( self ) -> str:
        return str( self.__value )
