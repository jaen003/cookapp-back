"""
 *
 * Libraries 
 *
"""

import os
import inspect
from types             import ModuleType
from importlib         import import_module
from src.shared.domain import DomainEventSubscriber

"""
 *
 * Class
 *
"""

class DomainEventSubscribersLocator:

    """
     *
     * Constants 
     *
    """
    
    __CONTEXT_MODULES_FOLDER_NAME   = 'src'
    __SHARED_KERNEL_FOLDER_NAME     = 'shared'
    __APPLICATION_LAYER_FOLDER_NAME = 'application'

    """
     *
     * Methods 
     *
    """

    def locate( self ) -> list[type]:
        # Variables
        subscriberClasses  : list[type]
        applicationModules : list[ModuleType]
        satisfiedClasses   : list[type]
        # Code
        applicationModules = self.__getApplicationModulesFromContext()
        subscriberClasses  = []
        for applicationModule in applicationModules:
            satisfiedClasses = inspect.getmembers( 
                applicationModule, 
                self.__isSubscriberClass                    
            )            
            subscriberClasses.extend( satisfiedClasses )
        return subscriberClasses
    
    def __isSubscriberClass( self, anyClass : object ) -> bool:
        return inspect.isclass( anyClass ) and \
            issubclass( anyClass, DomainEventSubscriber ) and \
            anyClass != DomainEventSubscriber

    def __getApplicationModulesFromContext( self ) -> list[ModuleType]:
        # Variables
        contextRootPath : str
        modules         : list[ModuleType]
        modulesPath     : str
        moduleName      : str
        module          : ModuleType
        # Code
        contextRootPath = os.path.abspath( os.curdir )
        modules         = []
        modulesPath = '{}/{}'.format( 
            contextRootPath, 
            self.__CONTEXT_MODULES_FOLDER_NAME 
        )
        with os.scandir( modulesPath ) as files:
            for file in files:
                if file.is_dir() and file.name != self.__SHARED_KERNEL_FOLDER_NAME:
                    moduleName = '{}.{}.{}'.format( 
                        self.__CONTEXT_MODULES_FOLDER_NAME,
                        file.name, 
                        self.__APPLICATION_LAYER_FOLDER_NAME 
                    )
                    module = import_module( moduleName )
                    modules.append( module )
        return modules