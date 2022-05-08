"""
 *
 * Libraries 
 *
"""

from src.shared.domain            import DomainException
from ..valueObjects.DiningTableId import DiningTableId

"""
 *
 * Classes 
 *
"""

class DiningTableNotFoundException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __DINING_TABLE_NOT_FOUND = 148

    """
     *
     * Methods 
     *
    """

    def __init__( self, id : DiningTableId ) -> None:
        super().__init__( 
            self.__DINING_TABLE_NOT_FOUND,
            'The dining table {} has not been found'.format( id.getValue() )
        )