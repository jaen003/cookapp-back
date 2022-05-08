"""
 *
 * Libraries 
 *
"""

from src.shared.domain                import DomainException
from ..valueObjects.DiningTableNumber import DiningTableNumber

"""
 *
 * Class 
 *
"""

class DiningTableNumberAlreadyCreatedException( DomainException ):

    """
     *
     * Constants 
     *
    """

    __DINING_TABLE_NUMBER_ALREADY_CREATED = 147

    """
     *
     * Methods 
     *
    """

    def __init__( self, number : DiningTableNumber ) -> None:
        super().__init__( 
            self.__DINING_TABLE_NUMBER_ALREADY_CREATED,
            'The dining table number {} has already been created'.format( number.getValue() )
        )