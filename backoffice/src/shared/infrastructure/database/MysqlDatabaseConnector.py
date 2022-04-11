"""
 *
 * Libraries 
 *
"""

import os
from mysql.connector.pooling    import MySQLConnectionPool
from mysql.connector.connection import MySQLConnection
from mysql.connector            import Error
from time                       import sleep

"""
 *
 * Classes 
 *
"""

class Singleton( type ):

    """
     *
     * Attributes 
     *
    """

    __instances = {}

    """
     *
     * Methods 
     *
    """

    def __call__( cls, *args, **kwargs ):
        if cls not in cls.__instances:
            instance = super().__call__( *args, **kwargs )
            cls.__instances[cls] = instance
        return cls.__instances[cls]

class MysqlDatabaseConnector( metaclass = Singleton ):

    """
     *
     * Constants
     *
    """

    __CONNECTION_POOL_NAME = 'backoffice_database_connection_pool'

    """
     *
     * Attributes 
     *
    """

    __connectionPool     : MySQLConnectionPool
    __rootConnection     : MySQLConnection
    __password           : str
    __user               : str
    __host               : str
    __database           : str
    __port               : str
    __connectionPoolSize : int
    __reconnectionTime   : int
    __poolResetSession   : bool

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        self.__connectionPool     = None
        self.__rootConnection     = None
        self.__password           = os.getenv( 'DATABASE_PASSWORD' )
        self.__user               = os.getenv( 'DATABASE_USER' )
        self.__database           = os.getenv( 'DATABASE_NAME' )
        self.__host               = os.getenv( 'DATABASE_HOST' )
        self.__port               = os.getenv( 'DATABASE_PORT' )
        self.__connectionPoolSize = int( os.getenv( 'DATABASE_CONNECTION_POOL_SIZE' ) )
        self.__reconnectionTime   = int( os.getenv( 'DATABASE_RECONNECTION_TIME' ) )
        self.__poolResetSession   = os.getenv( 'DATABASE_POOL_RESET_SESSION' )

    def __getConcectionPool( self ) -> MySQLConnectionPool:
        while not self.__connectionPool:
            try:            
                self.__connectionPool = MySQLConnectionPool(
                    pool_name          = self.__CONNECTION_POOL_NAME,
                    pool_size          = self.__connectionPoolSize,
                    pool_reset_session = self.__poolResetSession,
                    host               = self.__host,
                    user               = self.__user,
                    password           = self.__password,
                    database           = self.__database,
                    port               = self.__port
                )
            except Error:
                sleep( self.__reconnectionTime )
        return self.__connectionPool

    def getConnectionString( self ) -> str:
        # Variables
        connectionString : str
        # Code
        connectionString = 'mysql://{}:{}@{}:{}/{}'.format( 
            self.__user, 
            self.__password, 
            self.__host, 
            self.__port,
            self.__database 
        )
        return connectionString

    def getConnection( self ) -> MySQLConnection:
        return self.__getConcectionPool().get_connection()

    def getRootConnection( self ) -> MySQLConnection:
        while not self.__rootConnection:
            try:            
                self.__rootConnection = MySQLConnection(
                    host     = self.__host,
                    user     = self.__user,
                    password = self.__password,
                    port     = self.__port
                )
            except Error:
                sleep( self.__reconnectionTime )
        return self.__rootConnection