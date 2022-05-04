"""
 *
 * Libraries 
 *
"""

from unittest               import TestCase
from src.diningTable.domain import DiningTableStatus

"""
 *
 * Class
 *
"""

class DiningTableStatusTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsEnabled( self ) -> None:
        # Variables
        valueObject : DiningTableStatus
        # Code
        valueObject = DiningTableStatus.createEnabled()
        self.assertEqual( valueObject.getValue(), 1 )
    
    def testIsDeleted( self ) -> None:
        # Variables
        valueObject : DiningTableStatus
        # Code
        valueObject = DiningTableStatus.createDeleted()
        self.assertEqual( valueObject.getValue(), 2 )