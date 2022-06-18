/* 
 * 
 * Libraries
 *
*/

using System.Data.SqlClient;
using preparation.src.diningTable.domain;
using preparation.src.restaurant.domain;
using preparation.src.shared.infrastructure;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.diningTable.infrastructure {

    public class MssqlDiningTableRepository : DiningTableRepository {

        /* 
         * 
         * Attributes
         *
        */

        MssqlDatabaseConnector databaseConnector;

        /* 
         * 
         * Methods
         *
        */

        public MssqlDiningTableRepository() {
            databaseConnector = MssqlDatabaseConnector.getInstance();
        }

        public bool save( DiningTable diningTable ) {
            // Variables
            String        query;
            SqlConnection connection;
            SqlCommand    command;
            // Code
            query = "INSERT INTO Dining_Table ( tab_id, tab_number, tab_status, " +
                    "rest_id ) VALUES ( @id, @number, @status, @restaurantId )";
            try {
                using( connection = databaseConnector.getConnection() ) {
                    using( command = new SqlCommand( query, connection ) ){
                        command.Parameters.AddWithValue( "@id", diningTable.getId().getValue() );
                        command.Parameters.AddWithValue( "@number", diningTable.getNumber().getValue() );
                        command.Parameters.AddWithValue( "@status", diningTable.getStatus().getValue() );
                        command.Parameters.AddWithValue( "@restaurantId", diningTable.getRestaurantId().getValue() );
                        connection.Open();
                        command.ExecuteNonQuery();
                    }
                }
                return true;
            } catch( SqlException exc ) {
                return false;
            }            
        }

        public bool update( DiningTable diningTable ) {
            // Variables
            String        query;
            SqlConnection connection;
            SqlCommand    command;
            // Code
            query = "UPDATE Dining_Table SET tab_number = @number, tab_status = @status " +
                    "WHERE tab_id = @id";
            try {
                using( connection = databaseConnector.getConnection() ) {
                    using( command = new SqlCommand( query, connection ) ){                        
                        command.Parameters.AddWithValue( "@number", diningTable.getNumber().getValue() );
                        command.Parameters.AddWithValue( "@status", diningTable.getStatus().getValue() );
                        command.Parameters.AddWithValue( "@id", diningTable.getId().getValue() );
                        connection.Open();
                        command.ExecuteNonQuery();
                    }
                }
                return true;
            } catch( SqlException exc ) {
                return false;
            }            
        }

        private DiningTable? mapEntity( SqlDataReader reader ) {
            // Variables
            DiningTable diningTable;
            // Code
            if( !reader.Read() ) {
                return null;
            }
            diningTable = new DiningTable(
                id           : new DiningTableId( reader["tab_id"].ToString() ),
                number       : new DiningTableNumber( Int32.Parse( reader["tab_number"].ToString() ) ),
                status       : new DiningTableStatus( Int32.Parse( reader["tab_status"].ToString() ) ),
                restaurantId : new RestaurantId( reader["rest_id"].ToString() )
            );
            return diningTable;
        }

        public DiningTable? findById( DiningTableId id ) {
            // Variables
            String        query;
            SqlConnection connection;
            SqlCommand    command;
            SqlDataReader reader;
            // Code
            query = "SELECT tab_id, tab_number, tab_status, rest_id " +
                    "FROM Dining_Table WHERE tab_status != 2 AND tab_id = @id";
            using( connection = databaseConnector.getConnection() ) {
                using( command = new SqlCommand( query, connection ) ){
                    command.Parameters.AddWithValue( "@id", id.getValue() );
                    connection.Open();
                    using( reader = command.ExecuteReader() ) {
                        return mapEntity( reader );
                    }
                }
            }            
        }

    }

}