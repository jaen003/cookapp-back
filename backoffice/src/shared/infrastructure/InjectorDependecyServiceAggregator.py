"""
 *
 * Libraries 
 *
"""

from injector import Binder
from injector import singleton
from flask    import request

"""
 *
 * Class
 *
"""

class InjectorDependecyServiceAggregator:

    """
     *
     * Methods 
     *
    """

    @classmethod
    def addSingleton( cls, binder : Binder, interface : object, to : object ) -> None:
        binder.bind( 
            interface = interface, 
            to        = to, 
            scope     = singleton 
        )

    @classmethod
    def addScope( cls, binder : Binder, interface : object, to : object ) -> None:
        binder.bind( 
            interface = interface, 
            to        = to, 
            scope     = request 
        )