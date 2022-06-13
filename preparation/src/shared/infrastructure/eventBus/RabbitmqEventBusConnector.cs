/* 
 * 
 * Libraries
 *
*/

using RabbitMQ.Client;
using RabbitMQ.Client.Exceptions;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class RabbitmqEventBusConnector { 

        /* 
         * 
         * Attributes
         *
        */

        private int               reconnectionTime;
        private string            user;
        private string            password;
        private string            host;
        private string            port;
        private IConnection?      connection;
        private ConnectionFactory connectionFactory;

        /* 
         * 
         * Methods
         *
        */ 

        public RabbitmqEventBusConnector() { 
            reconnectionTime = Int32.Parse( Environment.GetEnvironmentVariable( 
                "EVENT_BUS_RECONNECTION_TIME"
            ) );
            user     = Environment.GetEnvironmentVariable( "EVENT_BUS_USER" );
            password = Environment.GetEnvironmentVariable( "EVENT_BUS_PASSWORD" );
            port     = Environment.GetEnvironmentVariable( "EVENT_BUS_PORT" );
            host     = Environment.GetEnvironmentVariable( "EVENT_BUS_HOST" );
            createConnectionFactory();
        }

        private void createConnectionFactory() {
            // Variables            
            string eventBusUri;
            // Code
            connectionFactory = new ConnectionFactory();
            eventBusUri = string.Format( 
                "amqp://{0}:{1}@{2}:{3}", 
                user, 
                password, 
                host, 
                port 
            );
            connectionFactory.Uri = new Uri( eventBusUri );
        }

        private IConnection getConnection() {            
            while( connection == null ) {
                try {                    
                    connection = connectionFactory.CreateConnection(); 
                } catch( BrokerUnreachableException ) {
                    Thread.Sleep( reconnectionTime );
                }
            }
            return connection;
        }

        public IModel getChannel() {
            return getConnection().CreateModel();
        }

    }

}
