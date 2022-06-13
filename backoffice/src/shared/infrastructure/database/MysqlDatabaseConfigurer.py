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
    __migrationsPath    : str

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        self.__databaseConnector = MysqlDatabaseConnector()
        self.__migrationsPath    = os.getenv( 'DATABASE_MIGRATIONS_PATH' )

    def __getMigrationBackend( self ) -> MySQLBackend:
        # Variables
        connectionString : str
        # Code
        connectionString = self.__databaseConnector.getConnectionString()
        return get_backend( connectionString )

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