"""
 *
 * Libraries 
 *
"""

from src.shared.domain                              import IntValueObject
from ..exceptions.InvalidDiningTableNumberException import InvalidDiningTableNumberException

"""
 *
 * Classes 
 *
"""

class DiningTableNumber( IntValueObject ):

    """
     *
     * Consts 
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
        if not self.isValid():
            raise InvalidDiningTableNumberException( value )
    
    def isValid( self ) -> bool:
        return self.isGreaterThanOrEqual( IntValueObject( self.__MINIMUN_NUMBER ) ) and \
            self.isLessThanOrEqual( IntValueObject( self.__MAXIMUM_NUMBER ) )