"""
 *
 * Libraries 
 *
"""

import inspect
import typing
from types                  import ModuleType
from src.shared.domain      import DomainEventSubscriber
from ..ContextModulesFinder import ContextModulesFinder

"""
 *
 * Class
 *
"""

class DomainEventSubscribersLocator:

    """
     *
     * Methods 
     *
    """

    @classmethod
    def locate( cls, eventClass : type ) -> list[type]:
        # Variables
        subscriberClasses  : list[type]
        applicationModules : list[ModuleType]
        satisfiedClasses   : list[type]
        # Code
        applicationModules = ContextModulesFinder.findApplicationModules()
        subscriberClasses  = []
        for applicationModule in applicationModules:
            satisfiedClasses = list( map( lambda members: members[1], inspect.getmembers( 
                applicationModule, 
                lambda anyClass: cls.__isSubscriberClass( anyClass, eventClass )                    
            ) ) )            
            subscriberClasses.extend( satisfiedClasses )
        return subscriberClasses
    
    @classmethod
    def __getEventClass( cls, eventSubscriberClass : type ) -> type:
        return typing.get_args( eventSubscriberClass.__orig_bases__[0] )[0]
    
    @classmethod
    def __isSubscriberClass( cls, anyClass : object, eventClass : type ) -> bool:
        return inspect.isclass( anyClass ) and \
            issubclass( anyClass, DomainEventSubscriber ) and \
            anyClass != DomainEventSubscriber and  \
            cls.__getEventClass( anyClass ) == eventClass