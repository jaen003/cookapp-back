"""
 *
 * Class
 *
"""

class DomainException( Exception ):

    """
     *
     * Attributes 
     *
    """

    __code : int

    """
     *
     * Methods 
     *
    """

    def __init__( self, code : int, message : str ) -> object:
        super().__init__( message )
        self.__code = code

    def getCode( self ) -> int:
        return self.__code