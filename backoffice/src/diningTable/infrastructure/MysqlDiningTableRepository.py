"""
 *
 * Libraries 
 *
"""

from src.diningTable.domain     import DiningTableDescription
from src.diningTable.domain     import DiningTable
from src.diningTable.domain     import DiningTableRepository
from src.diningTable.domain     import DiningTableNumber
from src.diningTable.domain     import DiningTableId
from src.diningTable.domain     import DiningTableStatus
from src.shared.infrastructure  import MysqlDatabaseConnector
from src.restaurant.domain      import RestaurantId
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor     import MySQLCursor

"""
 *
 * Class 
 *
"""

class MysqlDiningTableRepository( DiningTableRepository ):

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

    def save( self, diningTable : DiningTable ) -> bool:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'INSERT INTO Dining_Table ( tab_id, tab_number, tab_description, ' \
                'tab_status, rest_id ) VALUES ( %s, %s, %s, %s, %s )'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                diningTable.getId().getValue(),
                diningTable.getNumber().getValue(),
                diningTable.getDescription().getValue(),
                diningTable.getStatus().getValue(),
                diningTable.getRestaurantId().getValue()
            )
            cursor.execute( query, values )
            connection.commit()
            return True
        except Exception:
            return False
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def update( self, diningTable : DiningTable ) -> bool:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'UPDATE Dining_Table SET tab_number = %s, tab_description = %s, ' \
                'tab_status = %s WHERE tab_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                diningTable.getNumber().getValue(),
                diningTable.getDescription().getValue(),
                diningTable.getStatus().getValue(),
                diningTable.getId().getValue(),
            )
            cursor.execute( query, values )
            connection.commit()
            return True
        except Exception:
            return False
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def mapEntity( self, record : list ) -> DiningTable:
        # Variables
        diningTable : DiningTable
        # Code
        if record is None:
            return None
        diningTable = DiningTable(
            id           = DiningTableId( record[0] ),
            number       = DiningTableNumber( record[1] ),
            description  = DiningTableDescription( record[2] ),
            status       = DiningTableStatus( record[3] ),
            restaurantId = RestaurantId( record[4] )
        )
        return diningTable
            
    def findByNumberAndRestaurant( self, number : DiningTableNumber, restaurantId : RestaurantId ) -> DiningTable:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT tab_id, tab_number, tab_description, tab_status, rest_id ' \
                'FROM Dining_Table WHERE tab_status != 2 AND tab_number = %s AND rest_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                number.getValue(),
                restaurantId.getValue(),
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
    
    def findByIdAndRestaurant( self, id : DiningTableId, restaurantId : RestaurantId ) -> DiningTable:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT tab_id, tab_number, tab_description, tab_status, rest_id ' \
                'FROM Dining_Table WHERE tab_status != 2 AND tab_id = %s AND rest_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                id.getValue(),
                restaurantId.getValue(),
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