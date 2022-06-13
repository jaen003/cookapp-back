/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class DomainEventsInformation {

        /* 
         * 
         * Attributes
         *
        */

        private List<DomainEventInformation> eventsInformation;

        /* 
         * 
         * Methods
         *
        */

        public DomainEventsInformation( 
            List<DomainEventInformation> eventsInformation 
        ) {
            this.eventsInformation = eventsInformation;
        }

        public List<DomainEventInformation> getAll() {
            return eventsInformation;
        }

        public DomainEventInformation findByEventName( string name ) {
            // Variables
            DomainEventInformation result;
            // Code
            result = null;
            foreach( DomainEventInformation eventInformation in eventsInformation ) {
                if( eventInformation.getEventName() == name ) {
                    result = eventInformation;
                }
            }
            return result;
        }

    }
}
