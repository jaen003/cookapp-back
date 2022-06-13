"""
 *
 * Libraries 
 *
"""

from src.shared.domain                              import IntValueObject
from ..exceptions.InvalidDiningTableNumberException import InvalidDiningTableNumberException

"""
 *
 * Class 
 *
"""

class DiningTableNumber( IntValueObject ):

    """
     *
     * Constants 
     *
    """

    __MINIMUN_NUMBER = 1
    __MAXIMUM_NUMBER = 255

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
        if not self.__isValid():
            raise InvalidDiningTableNumberException( value )
    
    def __isValid( self ) -> bool:
        return self.isGreaterThanOrEqual( IntValueObject( self.__MINIMUN_NUMBER ) ) and \
            self.isLessThanOrEqual( IntValueObject( self.__MAXIMUM_NUMBER ) )