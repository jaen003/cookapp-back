"""
 *
 * Libraries 
 *
"""

import os
import inspect
from flask                     import Flask
from flask_cors                import CORS
from src.shared.infrastructure import RabbitmqEventBusConfigurer
from src.shared.infrastructure import RabbitmqDomainEventsConsumer
from src.shared.infrastructure import RabbitmqDomainEventsPublisher
from src.shared.infrastructure import MysqlDatabaseConfigurer
from src.shared.domain         import DomainEventsPublisher
from injector                  import Binder
from injector                  import Injector
from src.shared.infrastructure import ConsumedDomainEventsAggregator
from src.shared.infrastructure import InjectorDependecyServiceAggregator
from types                     import ModuleType
from importlib                 import import_module
from flask_classful            import FlaskView

"""
 *
 * Global variables 
 *
"""

app             = Flask( __name__ )
controllersPath = os.getenv( 'CONTROLLERS_PATH' )

"""
 *
 * Methods 
 *
"""

def isControllerClass( anyClass : object ) -> bool :
        return inspect.isclass( anyClass ) and issubclass( anyClass, FlaskView ) and \
            anyClass != FlaskView
    
def addControllers( injector : Injector ) -> None:
    # Variables
    domainEventPublisher  : DomainEventsPublisher
    satisfiedClasses      : list[type]
    controllersModule     : ModuleType
    controllersModuleName : str
    # Code
    controllersModuleName = controllersPath.replace( '/', '.' )
    domainEventPublisher  = injector.get( DomainEventsPublisher )
    controllersModule     = import_module( controllersModuleName )
    satisfiedClasses      = inspect.getmembers( controllersModule, isControllerClass )
    for _, controllerClass in satisfiedClasses:
        controllerClass.register( app, init_argument = domainEventPublisher )

def initServices( injector : Injector ) -> None:
    # Variables
    eventBusConfigurer          : RabbitmqEventBusConfigurer
    rabbitmqDomainEventConsumer : RabbitmqDomainEventsConsumer
    mysqlDatabaseConfigurer     : MysqlDatabaseConfigurer
    # Code
    eventBusConfigurer          = injector.get( RabbitmqEventBusConfigurer )
    rabbitmqDomainEventConsumer = injector.get( RabbitmqDomainEventsConsumer )
    mysqlDatabaseConfigurer     = MysqlDatabaseConfigurer()
    eventBusConfigurer.configure()
    mysqlDatabaseConfigurer.configure()
    rabbitmqDomainEventConsumer.consume()

def addServices( binder : Binder ) -> None:
    InjectorDependecyServiceAggregator.addScope( 
        binder, 
        DomainEventsPublisher, 
        RabbitmqDomainEventsPublisher
    )

def main() -> None:
    injector = Injector( [addServices, ConsumedDomainEventsAggregator] )
    initServices( injector )
    addControllers( injector )
    CORS( app, resources = { r"/api/*" : { "origins" : "*" } } )

main() # call the main method