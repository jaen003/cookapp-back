/* 
 * 
 * Libraries 
 *
*/

using System.Data.SqlClient;

/* 
 * 
 * Class 
 *
*/

namespace preparation.src.shared.infrastructure {

    public class MssqlDatabaseConnector {

        /* 
         * 
         * Attributes
         *
        */

        private static MssqlDatabaseConnector? instance;
        private                         string user;
        private                         string password;
        private                         string host;
        private                         string port;
        private                         string database;
        private                 SqlConnection? connection;
        private                        string? connectionString;

        /* 
         * 
         * Methods
         *
        */

        private MssqlDatabaseConnector() { 
            user     = Environment.GetEnvironmentVariable( "DATABASE_USER" );
            password = Environment.GetEnvironmentVariable( "SA_PASSWORD" );
            port     = Environment.GetEnvironmentVariable( "DATABASE_PORT" );
            host     = Environment.GetEnvironmentVariable( "DATABASE_HOST" );
            database = Environment.GetEnvironmentVariable( "DATABASE_NAME" );
        }

        public static MssqlDatabaseConnector getInstance() {
            if( instance == null ) {
                instance = new MssqlDatabaseConnector();
            }
            return instance;
        }

        private string getConnectionString() {
            if( connectionString == null ) {
                connectionString = string.Format( 
                    "Data Source={0},{1};Initial Catalog={2};User ID={3};Password={4}",
                    host,
                    port,
                    database,
                    user,
                    password
                );
            }
            return connectionString;
        }

        public SqlConnection getConnection() {
            // Variables
            string connectionString;
            // Code
            connectionString = getConnectionString();
            return new SqlConnection( connectionString );
        }

    }

}