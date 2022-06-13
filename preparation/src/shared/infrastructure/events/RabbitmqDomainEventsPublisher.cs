/* 
 * 
 * Libraries
 *
*/

using System.Text;
using preparation.src.shared.domain;
using RabbitMQ.Client;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class RabbitmqDomainEventsPublisher { 

        /* 
         * 
         * Attributes
         *
        */

        private RabbitmqEventBusConnector eventBusConnector;
        private int                       messageDeliveryMode;

        /* 
         * 
         * Methods
         *
        */

        public RabbitmqDomainEventsPublisher( RabbitmqEventBusConnector eventBusConnector ) {
            this.eventBusConnector = eventBusConnector;
            messageDeliveryMode = Int32.Parse( Environment.GetEnvironmentVariable( 
                "EVENT_BUS_MESSAGE_DELIVERY_MODE"
            ) );
        }

        public async Task publish( List<DomainEvent> domainEvents ) {
            foreach( DomainEvent domainEvent in domainEvents ) {
                await Task.Run( () => {
                    publishEvent( domainEvent );
                } );
            }
        }

        private void publishEvent( DomainEvent domainEvent ) {
            // Variables
            string messageBody;
            string eventName;
            // Code
            messageBody = JsonDomainEventSerializer.serialize( domainEvent );
            eventName   = domainEvent.getEventName();
            sendMessage( eventName, messageBody );
        }

        private void sendMessage( string exchangeName, string body ) {
            // Variables
            IModel           channel;
            IBasicProperties properties;
            // code
            channel    = eventBusConnector.getChannel();
            properties = channel.CreateBasicProperties();
            properties.DeliveryMode = ( byte )messageDeliveryMode;
            channel.BasicPublish(
                exchange        : exchangeName,
                routingKey      : "", 
                body            : UTF8Encoding.UTF8.GetBytes( body ), 
                basicProperties : properties
            );
            channel.Close();
        }
    
    }

}