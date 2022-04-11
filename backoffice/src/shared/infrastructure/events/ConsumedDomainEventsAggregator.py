"""
 *
 * Libraries 
 *
"""

import typing
from .DomainEventsInformation             import DomainEventsInformation
from .DomainEventInformation              import DomainEventInformation
from .DomainEventSubscribersLocator       import DomainEventSubscribersLocator
from injector                             import Module
from ..InjectorDependecyServiceAggregator import InjectorDependecyServiceAggregator

"""
 *
 * Class
 *
"""

class ConsumedDomainEventsAggregator( Module ):

    """
     *
     * Attributes
     *
    """

    __eventsubscribersLocator : DomainEventSubscribersLocator

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        self.__eventsubscribersLocator = DomainEventSubscribersLocator()

    def configure( self, binder ) -> None:
        # Variables
        eventInformationClasses : dict[type, list[type]]
        eventClass              : type
        eventsInformation       : list[DomainEventInformation]
        eventSubscriberClasses  : list[type]
        # Code        
        eventInformationClasses = {}
        eventSubscriberClasses  = self.__eventsubscribersLocator.locate()
        for _, eventSubscriberClass in eventSubscriberClasses:
            eventClass = self.__getEventClass( eventSubscriberClass )
            if eventClass in eventInformationClasses:
                eventInformationClasses[eventClass].append( eventSubscriberClass )
            else:
                eventInformationClasses[eventClass] = [eventSubscriberClass]                        
        eventsInformation = []                    
        for eventClass, eventSubscriberClasses in eventInformationClasses.items():
            eventsInformation.append( DomainEventInformation( 
                eventClass, 
                eventSubscriberClasses 
            ) )
        InjectorDependecyServiceAggregator.addSingleton( 
            binder, 
            DomainEventsInformation, 
            DomainEventsInformation( eventsInformation ) 
        )
    
    def __getEventClass( self, eventSubscriberClass : type ) -> type:
        return typing.get_args( eventSubscriberClass.__orig_bases__[0] )[0]