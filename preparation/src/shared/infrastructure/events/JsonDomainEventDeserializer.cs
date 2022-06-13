/* 
 * 
 * Libraries
 *
*/

using Newtonsoft.Json;
using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class JsonDomainEventDeserializer { 

        /* 
         * 
         * Attributes
         *
        */

        private DomainEventsInformation eventsInformation;

        /* 
         * 
         * Methods
         *
        */

        public JsonDomainEventDeserializer( DomainEventsInformation eventsInformation ) {
            this.eventsInformation = eventsInformation;
        }

        public DomainEvent deserialize( string messageBody ) {
            // Variables
            Dictionary<string, object> messageData;
            Type                       eventClass;
            string                     eventName;
            DomainEvent                domainEvent;
            DomainEventInformation     eventInformation;
            Dictionary<string, object> data;
            // Code
            messageData      = JsonConvert.DeserializeObject<Dictionary<string, object>>( messageBody );
            eventName        = messageData["name"].ToString();
            eventInformation = eventsInformation.findByEventName( eventName );
            eventClass       = eventInformation.getEventClass();
            domainEvent      = ( DomainEvent )Activator.CreateInstance( eventClass );
            data             = JsonConvert.DeserializeObject<Dictionary<string, object>>( messageData["data"].ToString() );
            domainEvent = ( DomainEvent )domainEvent.fromPrimitives( 
                eventId   : messageData["id"].ToString(), 
                timestamp : Int32.Parse( messageData["timestamp"].ToString() ),
                data      : data
            );
            return domainEvent;
        }
    
    }

}