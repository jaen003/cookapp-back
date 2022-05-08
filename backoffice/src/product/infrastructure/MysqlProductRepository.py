"""
 *
 * Libraries 
 *
"""

from src.product.domain         import Product
from src.product.domain         import ProductName
from src.product.domain         import ProductRepository
from src.product.domain         import ProductId
from src.restaurant.domain      import RestaurantId
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor     import MySQLCursor
from src.product.domain         import ProductPrice
from src.product.domain         import ProductDescription
from src.product.domain         import ProductStatus
from src.shared.infrastructure  import MysqlDatabaseConnector

"""
 *
 * Class
 *
"""

class MysqlProductRepository( ProductRepository ):

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

    def save( self, product : Product ) -> bool:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'INSERT INTO Product ( prod_id, prod_name, prod_price, ' \
                'prod_description, prod_status, rest_id ) ' \
                'VALUES ( %s, %s, %s, %s, %s, %s )'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                product.id().getValue(),
                product.name().getValue(),
                product.price().getValue(),
                product.description().getValue(),
                product.status().getValue(),
                product.restaurantId().getValue(),
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
                
    def update( self, product : Product ) -> bool:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'UPDATE Product SET prod_name = %s, prod_price = %s, ' \
                'prod_status = %s, prod_description = %s WHERE prod_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = ( 
                product.name().getValue(),
                product.price().getValue(),
                product.status().getValue(),
                product.description().getValue(),
                product.id().getValue(),
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

    def __mapEntity( self, record : list ) -> Product:
        # Variables
        product : Product
        # Code
        if record is None:
            return None
        product = Product(
            id           = ProductId( record[0] ),
            name         = ProductName( record[1] ),
            price        = ProductPrice( record[2] ),
            description  = ProductDescription( record[3] ),
            status       = ProductStatus( record[4] ),
            restaurantId = RestaurantId( record[5] ),
        )
        return product

    def findByIdAndRestaurant( self, id : ProductId, restaurantId : RestaurantId ) -> Product:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT prod_id, prod_name, prod_price, prod_description, prod_status, rest_id ' \
                'FROM Product WHERE prod_status != 2 and prod_id = %s and rest_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                id.getValue(),
                restaurantId.getValue(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            return self.__mapEntity( record )
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()
    
    def findByNameAndRestaurant( self, name : ProductName, restaurantId : RestaurantId ) -> Product:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT prod_id, prod_name, prod_price, prod_description, prod_status, rest_id ' \
                'FROM Product WHERE prod_status != 2 and prod_name = %s and rest_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                name.getValue(),
                restaurantId.getValue(),
            )
            cursor.execute( query, values )
            record = cursor.fetchone()
            return self.__mapEntity( record )
        except Exception:
            return None
        finally:
            if connection is not None:
                cursor.close()
                connection.close()