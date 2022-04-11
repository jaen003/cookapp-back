"""
 *
 * Libraries 
 *
"""

from abc          import abstractmethod
from abc          import ABCMeta
from .DomainEvent import DomainEvent

"""
 *
 * Interface
 *
"""

class DomainEventsPublisher( metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """

    @abstractmethod
    def publish( self, domainEvents : list[DomainEvent] ) -> None:
        pass