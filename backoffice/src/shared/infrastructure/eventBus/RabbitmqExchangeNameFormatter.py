"""
 *
 * Class
 *
"""

class RabbitmqExchangeNameFormatter:

    """
     *
     * Methods 
     *
    """

    def formatDeadLetter( self, eventName : str ) -> str:
        return 'dead.letter.{}'.format( eventName )