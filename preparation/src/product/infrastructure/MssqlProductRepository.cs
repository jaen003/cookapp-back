/* 
 * 
 * Libraries
 *
*/

using System.Data.SqlClient;
using preparation.src.product.domain;
using preparation.src.shared.infrastructure;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.product.infrastructure {

    public class MssqlProductRepository : ProductRepository {

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

        public MssqlProductRepository() {
            databaseConnector = MssqlDatabaseConnector.getInstance();
        }

        public bool save( Product product ) {
            // Variables
            String        query;
            SqlConnection connection;
            SqlCommand    command;
            // Code
            query = "INSERT INTO Product ( prod_id, prod_name, prod_status ) " +
                    "VALUES ( @id, @name, @status )";
            try {
                using( connection = databaseConnector.getConnection() ) {
                    using( command = new SqlCommand( query, connection ) ){
                        command.Parameters.AddWithValue( "@id", product.getId().getValue() );
                        command.Parameters.AddWithValue( "@name", product.getName().getValue() );
                        command.Parameters.AddWithValue( "@status", product.getStatus().getValue() );
                        connection.Open();
                        command.ExecuteNonQuery();
                    }
                }
                return true;
            } catch( SqlException exc ) {
                return false;
            }            
        }

        public bool update( Product product ) {
            // Variables
            String        query;
            SqlConnection connection;
            SqlCommand    command;
            // Code
            query = "UPDATE Product SET prod_name = @name, prod_status = @status " +
                    "WHERE prod_id = @id";
            try {
                using( connection = databaseConnector.getConnection() ) {
                    using( command = new SqlCommand( query, connection ) ){
                        command.Parameters.AddWithValue( "@name", product.getName().getValue() );
                        command.Parameters.AddWithValue( "@status", product.getStatus().getValue() );
                        command.Parameters.AddWithValue( "@id", product.getId().getValue() );
                        connection.Open();
                        command.ExecuteNonQuery();
                    }
                }
                return true;
            } catch( SqlException exc ) {
                return false;
            }            
        }        

        private Product? mapEntity( SqlDataReader reader ) {
            // Variables
            Product product;
            // Code
            if( !reader.Read() ) {
                return null;
            }
            product = new Product(
                id     : new ProductId( reader["prod_id"].ToString() ),
                name   : new ProductName( reader["prod_name"].ToString() ),
                status : new ProductStatus( Int32.Parse( reader["prod_status"].ToString() ) )
            );
            return product;
        }

        public Product? findById( ProductId id ) {
            // Variables
            String        query;
            SqlConnection connection;
            SqlCommand    command;
            SqlDataReader reader;
            // Code
            query = "SELECT prod_id, prod_name, prod_status " +
                    "FROM Product WHERE prod_status != 2 AND prod_id = @id";
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