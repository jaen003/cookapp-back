/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.domain {

    public class AggregateRoot {

        /* 
         * 
         * Attributes
         *
        */

        private List<DomainEvent> domainEvents;

        /* 
         * 
         * Methods
         *
        */

        public AggregateRoot() {
            domainEvents = new List<DomainEvent>();
        }

        public void recordEvent( DomainEvent domainEvent ) {
            domainEvents.Add( domainEvent );
        }

        public List<DomainEvent> pullEvents() {
            // Variables
            List<DomainEvent> events;
            // Code
            events  = domainEvents;
            domainEvents = new List<DomainEvent>();
            return events;
        }

    }

}