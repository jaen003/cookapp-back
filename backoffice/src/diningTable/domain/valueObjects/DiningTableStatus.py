"""
 *
 * Libraries 
 *
"""

from src.shared.domain import IntValueObject

"""
 *
 * Classes 
 *
"""

class DiningTableStatus( IntValueObject ):

    """
     *
     * Constants 
     *
    """

    __ENABLED  = 1
    __DELETED  = 2

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> None:
        super().__init__( value )
    
    @classmethod
    def createEnabled( cls ) -> object:
        return cls( cls.__ENABLED )
    
    @classmethod
    def createDeleted( cls ) -> object:
        return cls( cls.__DELETED )