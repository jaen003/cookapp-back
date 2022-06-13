/* 
 * 
 * Class 
 *
*/

namespace preparation.src.shared.domain {

    public abstract class DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private string eventId;
        private int    timestamp;

        /* 
         * 
         * Methods
         *
        */

        public DomainEvent( string eventId, int timestamp ) {
            this.eventId   = eventId;
            this.timestamp = timestamp;
        }

        public DomainEvent() {
            eventId   = generateId();
            timestamp = getTimestamp();
        }

        private string generateId() {
            return Guid.NewGuid().ToString();
        }

        private int generateTimestamp() {
            // Variables
            DateTime now;
            int      timestamp;
            // Code
            now       = DateTime.UtcNow;
            timestamp = ( int )( now.Subtract( new DateTime( 1970, 1, 1 ) ) ).TotalSeconds;
            return timestamp;
        }

        public string getEventId() {
            return eventId;
        }

        public int getTimestamp() {
            return timestamp;
        }

        public abstract string getEventName();

        public abstract Dictionary<string,object> toPrimitives();

        public abstract DomainEvent fromPrimitives( 
            string                    eventId, 
            int                       timestamp,
            Dictionary<string,object> data
        );

    }

}