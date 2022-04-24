"""
 *
 * Libraries 
 *
"""

from src.restaurant.domain      import RestaurantRepository
from src.restaurant.domain      import RestaurantName
from src.restaurant.domain      import RestaurantStatus
from src.restaurant.domain      import Restaurant
from src.shared.infrastructure  import MysqlDatabaseConnector
from src.restaurant.domain      import RestaurantId
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor     import MySQLCursor

"""
 *
 * Classes 
 *
"""

class MysqlRestaurantRepository( RestaurantRepository ):

    """
     *
     * Attributes 
     *
    """

    __databaseConnector : MysqlDatabaseConnector

    """
     *
     * Methods 
     *
    """

    def __init__( self ) -> object:
        self.__databaseConnector = MysqlDatabaseConnector()
    
    def mapEntity( self, record : list ) -> Restaurant:
        # Variables
        restaurant : Restaurant
        # Code
        if record is None:
            return None
        restaurant = Restaurant(
            id     = RestaurantId( record[0] ),
            name   = RestaurantName( record[1] ),
            status = RestaurantStatus( record[2] )
        )
        return restaurant
            
    def findById( self, id : RestaurantId ) -> Restaurant:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT rest_id, rest_name, rest_status FROM Restaurant ' \
                'WHERE rest_status = 1 and rest_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                id.getValue(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            return self.mapEntity( record )
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()