"""
 *
 * Libraries 
 *
"""

from unittest               import TestCase
from src.diningTable.domain import DiningTableDescription

"""
 *
 * Class
 *
"""

class DiningTableDescriptionTest( TestCase ):

    """
     *
     * Methods 
     *
    """

    def testIsNoneValue( self ) -> None:
        # Variables
        valueObject  : DiningTableDescription
        # Code
        valueObject = DiningTableDescription()
        self.assertEqual(valueObject.getValue(), 'No information' )
    
    def testIsNoneValue2( self ) -> None:
        # Variables
        valueObject  : DiningTableDescription
        # Code
        valueObject = DiningTableDescription( None )
        self.assertEqual(valueObject.getValue(), 'No information' )