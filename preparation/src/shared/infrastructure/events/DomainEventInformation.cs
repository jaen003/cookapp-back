/* 
 * 
 * Libraries
 *
*/

using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class DomainEventInformation {

        /* 
         * 
         * Attributes
         *
        */

        private List<Type> subscriberClasses;
        private Type       eventClass;

        /* 
         * 
         * Methods
         *
        */

        public DomainEventInformation( 
            Type       eventClass, 
            List<Type> subscriberClasses
        ) {
            this.subscriberClasses = subscriberClasses;
            this.eventClass        = eventClass;
        }

        public List<Type> getSubscriberClasses() {
            return subscriberClasses;
        }

        public Type getEventClass() {
            return eventClass;
        }

        public string getEventName() {
            // Variables
            DomainEvent domainEvent;
            string      eventName;
            // Code
            domainEvent = ( DomainEvent )Activator.CreateInstance( eventClass );
            eventName   = domainEvent.getEventName();
            return eventName;
        }

        public string formatRabbitmqQueueName() {
            return string.Format( "preparation.{0}", getEventName() );
        }

        public bool isConsumedEvent() {
            return subscriberClasses.Count > 0;
        }

    }
}
