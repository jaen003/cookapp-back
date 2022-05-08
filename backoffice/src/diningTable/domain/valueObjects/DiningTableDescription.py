"""
 *
 * Libraries 
 *
"""

from src.shared.domain import StringValueObject

"""
 *
 * Class 
 *
"""

class DiningTableDescription( StringValueObject ):

    """
     *
     * Methods 
     *
    """
    
    def __init__( self, value : str = None ) -> None:
        if not value:
            value = 'No information'
        super().__init__( value )