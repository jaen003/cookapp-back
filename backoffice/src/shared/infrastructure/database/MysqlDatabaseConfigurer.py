"""
 *
 * Libraries 
 *
"""

import os
from yoyo                       import read_migrations
from yoyo                       import get_backend
from .MysqlDatabaseConnector    import MysqlDatabaseConnector
from pymysql.err                import OperationalError
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor     import MySQLCursor
from yoyo.backends              import MySQLBackend
from yoyo.migrations            import MigrationList

"""
 *
 * Class
 *
"""

class MysqlDatabaseConfigurer:

    """
     *
     * Attributes 
     *
    """

    __databaseConnector : MysqlDatabaseConnector
    __databaseName      : str
    __migrationsPath    : str

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        self.__databaseConnector = MysqlDatabaseConnector()
        self.__databaseName      = os.getenv( 'DATABASE_NAME' )
        self.__migrationsPath    = os.getenv( 'DATABASE_MIGRATIONS_PATH' )
    
    def __createDatabase( self ) -> None:
        # Variables
        connection : MySQLConnection
        query      : str
        cursor     : MySQLCursor
        # Code
        query = 'CREATE DATABASE {}'.format(
            self.__databaseName
        )
        connection = self.__databaseConnector.getRootConnection()
        cursor     = connection.cursor()
        cursor.execute( query )

    def __getMigrationBackend( self ) -> MySQLBackend:
        # Variables
        connectionString : str
        backend          : MySQLBackend
        # Code        
        backend          = None
        connectionString = self.__databaseConnector.getConnectionString()
        while not backend:
            try:
                backend = get_backend( connectionString )
            except OperationalError:
                self.__createDatabase()
        return backend

    def __applyMigrations( self ) -> None:
        # Variables
        backend    : MySQLBackend
        migrations : MigrationList
        # Code      
        backend    = self.__getMigrationBackend()  
        migrations = read_migrations( self.__migrationsPath )
        with backend.lock():
            backend.apply_migrations( backend.to_apply( migrations ) )
    
    def configure( self ) -> None:
        self.__applyMigrations()