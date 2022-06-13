/* 
 * 
 * Libraries
 *
*/

using RabbitMQ.Client;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class RabbitmqEventBusConfigurer { 

        /* 
         * 
         * Attributes
         *
        */

        private RabbitmqEventBusConnector     eventBusConnector;
        private DomainEventsInformation       eventsInformation;
        private RabbitmqQueueNameFormatter    queueNameFormatter;
        private RabbitmqExchangeNameFormatter exchangeNameFormatter;

        /* 
         * 
         * Methods
         *
        */

        public RabbitmqEventBusConfigurer( 
            RabbitmqEventBusConnector     eventBusConnector,
            DomainEventsInformation       eventsInformation,
            RabbitmqQueueNameFormatter    queueNameFormatter,
            RabbitmqExchangeNameFormatter exchangeNameFormatter 
        ) {
            this.eventBusConnector     = eventBusConnector;
            this.eventsInformation     = eventsInformation;
            this.queueNameFormatter    = queueNameFormatter;
            this.exchangeNameFormatter = exchangeNameFormatter;
        }

        public void configure() {
            // Variables
            string eventName;
            string queueName;
            string deadLetterQueueName;
            string deadLetterExchangeName;
            // Code
            foreach( DomainEventInformation eventInformation in eventsInformation.getAll() ) {
                eventName = eventInformation.getEventName();
                declareExchange( eventName );
                if( eventInformation.isConsumedEvent() ) {
                    queueName = queueNameFormatter.format( eventInformation );
                    declareQueue( queueName );
                    bindQueue( queueName, eventName );
                    deadLetterQueueName    = queueNameFormatter.formatDeadLetter( eventInformation );
                    deadLetterExchangeName = exchangeNameFormatter.formatDeadLetter( eventName );
                    declareQueue( deadLetterQueueName );
                    declareExchange( deadLetterExchangeName );
                    bindQueue( deadLetterQueueName, deadLetterExchangeName ) ;
                }
            }
        }

        private void declareExchange( string exchangeName ) {
            // Variables
            IModel channel;
            // code
            channel = eventBusConnector.getChannel();
            channel.ExchangeDeclare(
                exchange : exchangeName, 
                type     : "fanout", 
                durable  : true
            );
            channel.Close();
        }

        private void bindQueue( string queueName, string exchangeName ) {
            // Variables
            IModel channel;
            // code
            channel = eventBusConnector.getChannel();
            channel.QueueBind(
                queue      : queueName,
                exchange   : exchangeName, 
                routingKey : "#"
            );
            channel.Close();
        }

        private void declareQueue( string queueName ) {
            // Variables
            IModel channel;
            // code
            channel = eventBusConnector.getChannel();
            channel.QueueDeclare(
                queue      : queueName,
                durable    : true,
                exclusive  : false,
                autoDelete : false
            );
            channel.Close();
        }

    }

}