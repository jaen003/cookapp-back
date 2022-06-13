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

    public class MssqlDatabaseConfigurer {

        /* 
         * 
         * Attributes
         *
        */

        private                 string migrationsPath;
        private MssqlDatabaseConnector databaseConnector;

        /* 
         * 
         * Methods
         *
        */

        public MssqlDatabaseConfigurer() {
            databaseConnector = MssqlDatabaseConnector.getInstance();
            migrationsPath    = Environment.GetEnvironmentVariable( "DATABASE_MIGRATIONS_PATH" );
        }

        private void applyMigrations() {
            // Variables
            SqlConnection databaseConnection;
            // Code
            databaseConnection = databaseConnector.getConnection();
            var evolve = new Evolve.Evolve( databaseConnection ) {
                Locations       = new[] { migrationsPath },
                IsEraseDisabled = true,
            };
            evolve.Migrate();
        }

        public void configure() {
            applyMigrations();
        }

    }

}