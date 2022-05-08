"""
 *
 * Libraries 
 *
"""

from src.employee.domain        import Employee
from src.employee.domain        import EmployeeRepository
from src.employee.domain        import EmployeeEmail
from src.employee.domain        import EmployeeName
from src.employee.domain        import EmployeeId
from src.employee.domain        import EmployeeRole
from src.employee.domain        import EmployeeStatus
from src.shared.infrastructure  import MysqlDatabaseConnector
from src.restaurant.domain      import RestaurantId
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor     import MySQLCursor

"""
 *
 * Class 
 *
"""

class MysqlEmployeeRepository( EmployeeRepository ):

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

    def save( self, employee : Employee ) -> bool:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'INSERT INTO Employee ( emp_id, emp_email, emp_name, emp_role, ' \
                'emp_status, rest_id ) VALUES ( %s, %s, %s, %s, %s, %s )'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                employee.getId().getValue(),
                employee.getEmail().getValue(),
                employee.getName().getValue(),
                employee.getRole().getValue(),
                employee.getStatus().getValue(),
                employee.getRestaurantId().getValue()
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
    
    def update( self, employee : Employee ) -> bool:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        # Code
        query = 'UPDATE Employee SET emp_email = %s, emp_name = %s, emp_role = %s, ' \
                'emp_status = %s WHERE emp_id = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                employee.getEmail().getValue(),
                employee.getName().getValue(),
                employee.getRole().getValue(),
                employee.getStatus().getValue(),
                employee.getId().getValue()
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
    
    def __mapEntity( self, record : list ) -> Employee:
        # Variables
        employee : Employee
        # Code
        if record is None:
            return None
        employee = Employee(
            id           = EmployeeId( record[0] ),
            email        = EmployeeEmail( record[1] ),
            name         = EmployeeName( record[2] ),
            role         = EmployeeRole( record[3] ),
            status       = EmployeeStatus( record[4] ),
            restaurantId = RestaurantId( record[5] )
        )
        return employee
            
    def findByNameAndRestaurant( self, name : EmployeeName, restaurantId : RestaurantId ) -> Employee:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT emp_id, emp_email, emp_name, emp_role, emp_status, rest_id ' \
                'FROM Employee WHERE emp_status != 2 AND emp_name = %s AND rest_id = %s'
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
    
    def findByIdAndRestaurant( self, id : EmployeeId, restaurantId : RestaurantId ) -> Employee:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT emp_id, emp_email, emp_name, emp_role, emp_status, rest_id ' \
                'FROM Employee WHERE emp_status != 2 AND emp_id = %s AND rest_id = %s'
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
    
    def findByEmail( self, email : EmployeeEmail ) -> Employee:
        # Variables
        query      : str
        values     : tuple
        connection : MySQLConnection
        cursor     : MySQLCursor
        record     : list
        # Code
        query = 'SELECT emp_id, emp_email, emp_name, emp_role, emp_status, rest_id ' \
                'FROM Employee WHERE emp_status != 2 AND emp_email = %s'
        try:
            connection = self.__databaseConnector.getConnection()
            cursor     = connection.cursor()
            values = (
                email.getValue(),
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