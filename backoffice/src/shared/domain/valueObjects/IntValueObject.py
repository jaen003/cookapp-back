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
    
    def equals( self, other : object ) -> bool:
        return self.__value == other.getValue()
    
    def isLessThan( self, other : object ) -> bool:
        return self.__value < other.getValue()
    
    def isGreaterThan( self, other : object ) -> bool:
        return self.__value > other.getValue()
    
    def isLessThanOrEqual( self, other : object ) -> bool:
        return self.__value <= other.getValue()
    
    def isGreaterThanOrEqual( self, other : object ) -> bool:
        return self.__value >= other.getValue()
    
    def toString( self ) -> str:
        return str( self.__value )
