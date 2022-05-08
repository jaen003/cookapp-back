"""
 *
 * Libraries 
 *
"""

from src.shared.domain import IntValueObject

"""
 *
 * Class 
 *
"""

class EmployeeStatus( IntValueObject ):

    """
     *
     * Constants 
     *
    """

    __ENABLED  = 1
    __DELETED  = 2
    __DISABLED = 3
    __BLOCKED  = 4

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
    
    @classmethod
    def createBlocked( cls ) -> object:
        return cls( cls.__BLOCKED )

    @classmethod
    def createDisabled( cls ) -> object:
        return cls( cls.__DISABLED )
    
    def isDisabled( self ) -> bool:
        return self.equals( IntValueObject( self.__DISABLED ) )
    
    def isBlocked( self ) -> bool:
        return self.equals( IntValueObject( self.__BLOCKED ) )