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

class EmployeeRole( IntValueObject ):

    """
     *
     * Constants 
     *
    """

    __CHEF   = 2
    __WAITER = 3

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : int ) -> object:
        super().__init__( value )
    
    @classmethod
    def createChef( cls ) -> object:
        return  cls( cls.__CHEF )
    
    @classmethod
    def createWaiter( cls ) -> object:
        return cls( cls.__WAITER )
    
    def isChef( self ) -> bool:
        return self.equals( IntValueObject( self.__CHEF ) )
    
    def isWaiter( self ) -> bool:
        return self.equals( IntValueObject( self.__WAITER ) )

