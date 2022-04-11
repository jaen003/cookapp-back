"""
 *
 * Libraries 
 *
"""

from abc    import abstractmethod
from abc    import ABCMeta
from typing import TypeVar
from typing import Generic

"""
 *
 * Interface
 *
"""

T = TypeVar( 'T' )

class DomainEventSubscriber( Generic[T], metaclass = ABCMeta ):

    """
     *
     * Methods 
     *
    """

    @abstractmethod
    def handleEvent( self, domainEvent : T ) -> None:
        pass