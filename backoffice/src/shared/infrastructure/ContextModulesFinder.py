"""
 *
 * Libraries 
 *
"""

import os
from types     import ModuleType
from importlib import import_module

"""
 *
 * Class
 *
"""

class ContextModulesFinder:

    @classmethod
    def findDomainModules( cls ) -> list[ModuleType]:
        return cls.__findModulesFromLayer( 'domain' )
    
    @classmethod
    def findApplicationModules( cls ) -> list[ModuleType]:
        return cls.__findModulesFromLayer( 'application' )
    
    @classmethod
    def __findModulesFromLayer( cls, layerName : str ) -> list[ModuleType]:
        # Variables
        contextRootPath : str
        modules         : list[ModuleType]
        modulesPath     : str
        moduleName      : str
        module          : ModuleType
        # Code
        contextRootPath = os.path.abspath( os.curdir )
        modules         = []
        modulesPath     = '{}/src'.format( contextRootPath )
        with os.scandir( modulesPath ) as files:
            for file in files:
                if file.is_dir() and file.name != 'shared':
                    moduleName = 'src.{}.{}'.format( file.name, layerName )
                    module     = import_module( moduleName )
                    modules.append( module )
        return modules