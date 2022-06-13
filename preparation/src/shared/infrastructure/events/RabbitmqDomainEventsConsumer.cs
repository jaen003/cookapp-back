/* 
 * 
 * Libraries
 *
*/

using System.Text;
using preparation.src.shared.domain;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class RabbitmqDomainEventsConsumer { 

        /* 
         * 
         * Constants
         *
        */

        private const string RETRY_COUNT_FIELD_NAME = "retryCount";

        /* 
         * 
         * Attributes
         *
        */

        private RabbitmqEventBusConnector     eventBusConnector;
        private DomainEventsInformation       eventsInformation;
        private RabbitmqExchangeNameFormatter exchangeNameFormatter;
        private JsonDomainEventDeserializer   domainEventDeserializer;
        private int                           messageDeliveryMode;
        private int                           maximumNumberOfRetries;
        private IServiceProvider              serviceProvider;

        /* 
         * 
         * Methods
         *
        */

        public RabbitmqDomainEventsConsumer( 
            RabbitmqEventBusConnector     eventBusConnector,
            DomainEventsInformation       eventsInformation,
            RabbitmqExchangeNameFormatter exchangeNameFormatter,
            JsonDomainEventDeserializer   domainEventDeserializer,
            IServiceProvider              serviceProvider 
        ) {
            this.eventBusConnector       = eventBusConnector;
            this.eventsInformation       = eventsInformation;
            this.exchangeNameFormatter   = exchangeNameFormatter;
            this.domainEventDeserializer = domainEventDeserializer;
            this.serviceProvider         = serviceProvider;
            messageDeliveryMode = Int32.Parse( Environment.GetEnvironmentVariable( 
                "EVENT_BUS_MESSAGE_DELIVERY_MODE"
            ) );
            maximumNumberOfRetries = Int32.Parse( Environment.GetEnvironmentVariable( 
                "MAXIMUM_NUMBER_OF_EVENT_BUS_RETRIES"
            ) );
        }

        public async Task consume() {
            foreach( DomainEventInformation eventInformation in eventsInformation.getAll() ) {
                if( eventInformation.isConsumedEvent() ) {
                    await Task.Run( () => {
                        consumeEvent( eventInformation );
                    } );
                }
            }
        }

        private void consumeEvent( DomainEventInformation eventInformation ) {
            // Variables
            IModel                    channel;
            EventingBasicConsumer     consumer;
            string                    queueName;
            DomainEvent               domainEvent;
            string                    body;
            byte[]                    message;
            DomainEventSubscriberBase eventSubscriber;
            IServiceScope             scope;
            // code
            channel   = eventBusConnector.getChannel();
            consumer  = new EventingBasicConsumer( channel );
            queueName = eventInformation.formatRabbitmqQueueName();
            scope     = serviceProvider.CreateScope();
            consumer.Received += async ( model, deliverEventArgs ) => {
                message     = deliverEventArgs.Body.ToArray();
                body        = Encoding.UTF8.GetString( message );
                domainEvent = domainEventDeserializer.deserialize( body );
                try {
                    foreach( Type subscriberClass in eventInformation.getSubscriberClasses() ) {
                        eventSubscriber = ( DomainEventSubscriberBase )scope.ServiceProvider.GetRequiredService( subscriberClass );
                        await eventSubscriber.handleEvent( domainEvent );
                    }
                } catch( DomainException ) {
                    handleConsumptionError( deliverEventArgs, domainEvent );
                }
                channel.BasicAck( deliverEventArgs.DeliveryTag, false );
            };
            channel.BasicConsume(
                queue    : queueName,
                autoAck  : false,
                consumer : consumer
            );
        }

        private void handleConsumptionError( 
            BasicDeliverEventArgs deliverEventArgs, 
            DomainEvent           domainEvent 
        ) {
            // Variables
            string eventName;
            // code
            eventName = domainEvent.getEventName();
            if( hasBeenRetriedTooMuch( deliverEventArgs ) ) {
                sentToDeatLetter( deliverEventArgs, eventName );
            } else {
                sendToRetry( deliverEventArgs, eventName );
            }
        }

        private void sendToRetry( 
            BasicDeliverEventArgs deliverEventArgs, 
            string                eventName
        ) {
            // Variables
            int              retryCount;
            string           messageBody;
            IBasicProperties messageProperties;
            IModel           channel;
            byte[]           message;
            // Code
            retryCount = getRetryCount( deliverEventArgs );
            channel    = eventBusConnector.getChannel();
            messageProperties = channel.CreateBasicProperties();
            messageProperties.DeliveryMode = ( byte )messageDeliveryMode;
            messageProperties.Headers = new Dictionary<string, object>() { {
                RETRY_COUNT_FIELD_NAME, ( retryCount + 1 )
            } };
            message     = deliverEventArgs.Body.ToArray();
            messageBody = Encoding.UTF8.GetString( message );
            sendMessage( eventName, messageBody, messageProperties );
            channel.Close();
        }

        private bool hasBeenRetriedTooMuch( BasicDeliverEventArgs deliverEventArgs ) {
            // Variables
            int retryCount;
            // Code
            retryCount = getRetryCount( deliverEventArgs );
            return retryCount >= ( maximumNumberOfRetries - 1 );
        }

        private int getRetryCount( BasicDeliverEventArgs deliverEventArgs ) {
            // Variables
            int                         retryCount;
            IDictionary<string, object> messageHeaders;
            // Code
            messageHeaders = deliverEventArgs.BasicProperties.Headers;
            retryCount     = 0;
            if( messageHeaders != null && 
                messageHeaders.ContainsKey( RETRY_COUNT_FIELD_NAME ) 
            ) {
                retryCount = ( int )messageHeaders[RETRY_COUNT_FIELD_NAME];
            }
            return retryCount;
        }

        private void sentToDeatLetter( 
            BasicDeliverEventArgs deliverEventArgs,
            string                eventName
        ) {
            // Variables
            string exchangeName;
            string messageBody;
            byte[] message;
            // Code
            message      = deliverEventArgs.Body.ToArray();
            messageBody  = Encoding.UTF8.GetString( message );
            exchangeName = exchangeNameFormatter.formatDeadLetter( eventName );
            sendMessage( exchangeName, messageBody );
        }

        private void sendMessage( 
            string            exchangeName, 
            string            body,
            IBasicProperties? properties = null 
        ) {
            // Variables
            IModel channel;
            // code
            channel = eventBusConnector.getChannel();
            if( properties == null ) {
                properties = channel.CreateBasicProperties();
                properties.DeliveryMode = ( byte )messageDeliveryMode;
            }
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