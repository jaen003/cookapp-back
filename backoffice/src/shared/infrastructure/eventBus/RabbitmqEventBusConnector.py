"""
 *
 * Libraries 
 *
"""

import os
from time      import sleep
from amqpstorm import Connection
from amqpstorm import AMQPError
from amqpstorm import Channel
from injector  import singleton

"""
 *
 * Class
 *
"""

@singleton
class RabbitmqEventBusConnector:

    """
     *
     * Attributes 
     *
    """

    __connection       : Connection
    __host             : str
    __user             : str
    __password         : str
    __port             : int
    __reconnectionTime : int

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        self.__connection       = None
        self.__password         = os.getenv( 'EVENT_BUS_PASSWORD' )
        self.__user             = os.getenv( 'EVENT_BUS_USER' )
        self.__port             = int( os.getenv( 'EVENT_BUS_PORT' ) )
        self.__host             = os.getenv( 'EVENT_BUS_HOST' )
        self.__reconnectionTime = int( os.getenv( 'EVENT_BUS_RECONNECTION_TIME' ) )
    
    def getChannel( self ) -> Channel:
        return self.__getConnection().channel()

    def __getConnection( self ) -> Connection:        
        while not self.__connection:
            try:
                self.__connection = Connection(
                    username = self.__user,
                    password = self.__password,
                    hostname = self.__host,
                    port     = self.__port
                )
            except AMQPError:
                sleep( self.__reconnectionTime )
        return self.__connection