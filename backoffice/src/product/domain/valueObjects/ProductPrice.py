"""
 *
 * Libraries 
 *
"""

from src.shared.domain                         import IntValueObject
from ..exceptions.InvalidProductPriceException import InvalidProductPriceException


"""
 *
 * Class 
 *
"""

class ProductPrice( IntValueObject ):

    """
     *
     * Constants 
     *
    """

    __MINIMUN_PRICE = 1

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
        if not self.__isValid():
            raise InvalidProductPriceException( value )
    
    def __isValid( self ) -> bool:
        return self.isGreaterThanOrEqual( IntValueObject( self.__MINIMUN_PRICE ) )