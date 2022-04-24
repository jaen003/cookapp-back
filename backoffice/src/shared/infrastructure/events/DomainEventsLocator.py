"""
 *
 * Libraries 
 *
"""

import inspect
from types                  import ModuleType
from src.shared.domain      import DomainEvent
from ..ContextModulesFinder import ContextModulesFinder

"""
 *
 * Class
 *
"""

class DomainEventsLocator:

    """
     *
     * Methods 
     *
    """

    @classmethod
    def locate( cls ) -> list[type]:
        # Variables
        eventClasses     : list[type]
        domainModules    : list[ModuleType]
        satisfiedClasses : list[type]        
        # Code
        domainModules = ContextModulesFinder.findDomainModules()
        eventClasses  = []
        for domainModule in domainModules:
            satisfiedClasses = list( map( lambda members: members[1], inspect.getmembers( 
                domainModule, 
                cls.__isEventClass                    
            ) ) )           
            eventClasses.extend( satisfiedClasses )
        return eventClasses
    
    @classmethod
    def __isEventClass( cls, anyClass : object ) -> bool:
        return inspect.isclass( anyClass ) and \
            issubclass( anyClass, DomainEvent ) and \
            anyClass != DomainEvent