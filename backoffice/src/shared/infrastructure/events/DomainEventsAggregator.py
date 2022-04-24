"""
 *
 * Libraries 
 *
"""

from .DomainEventsInformation             import DomainEventsInformation
from .DomainEventInformation              import DomainEventInformation
from .DomainEventSubscribersLocator       import DomainEventSubscribersLocator
from .DomainEventsLocator                 import DomainEventsLocator
from injector                             import Module
from ..InjectorDependecyServiceAggregator import InjectorDependecyServiceAggregator

"""
 *
 * Class
 *
"""

class DomainEventsAggregator( Module ):

    """
     *
     * Methods 
     *
    """

    def configure( self, binder ) -> None:
        # Variables
        eventsInformation      : list[DomainEventInformation]
        eventSubscriberClasses : list[type]
        eventClasses           : list[type]
        # Code        
        eventsInformation = []
        eventClasses      = DomainEventsLocator.locate()
        for eventClass in eventClasses:
            eventSubscriberClasses = DomainEventSubscribersLocator.locate( eventClass )
            eventsInformation.append( DomainEventInformation( 
                eventClass, 
                eventSubscriberClasses 
            ) )
        InjectorDependecyServiceAggregator.addSingleton( 
            binder, 
            DomainEventsInformation, 
            DomainEventsInformation( eventsInformation ) 
        )