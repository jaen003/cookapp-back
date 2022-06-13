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

    def isEmpty( self ) -> bool:
        return self.__value == ''
    
    def equals( self, other : object ) -> bool:
        return self.__value == other.getValue()
    
    def isLongerThan( self, other : object ) -> bool:
        return len( self.__value ) > len( other.getValue() )
    
    def isLongerThanOrEqual( self, other : object ) -> bool:
        return len( self.__value ) >= len( other.getValue() )
