"""
 *
 * Libraries 
 *
"""

from ..events.DomainEventInformation import DomainEventInformation

"""
 *
 * Class
 *
"""

class RabbitmqQueueNameFormatter:

    """
     *
     * Methods 
     *
    """

    def format( self, eventInformation : DomainEventInformation ) -> str:
        return eventInformation.formatRabbitmqQueueName()

    def formatDeadLetter( self, eventInformation : DomainEventInformation ) -> str:
        return 'dead.letter.{}'.format( self.format( eventInformation ) )