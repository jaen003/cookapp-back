"""
 *
 * Libraries 
 *
"""

from uuid import uuid4

"""
 *
 * Class 
 *
"""

class UuidValueObject:

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

    def __init__( self, value : str = None ) -> object:
        if value is None:
            value = self.__generateValue()
        self.__value = value
    
    def __generateValue( self ) -> str:
        return str( uuid4() )

    def getValue( self ) -> str:
        return self.__value

    def isEmpty( self ) -> bool:
        return self.__value == ''
    
    def equals( self, other : object ) -> bool:
        return self.__value == other.getValue()
