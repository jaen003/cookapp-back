"""
 *
 * Class 
 *
"""

class StringValueObject:

    """
     *
     * Attributes 
     *
    """

    __value : str

    """
     *
     * Methods 
     *
    """

    def __init__( self, value : str ) -> object:
        self.__value = value
    
    def getValue( self ) -> str:
        return self.__value
    
    def __isAnComparableObject( self, other : object ) -> bool:
        return ( other is not None and issubclass( type( self ), type( other ) ) )

    def isEmpty( self ) -> bool:
        return ( self.__value is None or self.__value == '' )
    
    def equals( self, other : object ) -> bool:
        # Variables
        equalObjects : bool
        # Code
        equalObjects = False
        if self.__isAnComparableObject( other ):
            equalObjects = self.__value == other.getValue()
        return equalObjects
    
    def isLongerThan( self, other : object ) -> bool:
        # Variables
        response : bool
        # Code
        response = False
        if self.__isAnComparableObject( other ):
            response = len( self.__value ) > len( other.getValue() )
        return response
    
    def isLongerThanOrEqual( self, other : object ) -> bool:
        # Variables
        response : bool
        # Code
        response = False
        if self.__isAnComparableObject( other ):
            response = len( self.__value ) >= len( other.getValue() )
        return response
