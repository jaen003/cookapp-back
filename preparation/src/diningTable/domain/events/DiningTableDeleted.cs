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

namespace preparation.src.diningTable.domain {

    public class DiningTableDeleted : DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private DiningTableId id;

        /* 
         * 
         * Methods
         *
        */

        public DiningTableDeleted() {
        }

        public DiningTableDeleted( DiningTableId id ) {
            this.id = id;
        }

        public DiningTableDeleted(
            DiningTableId id,
            string        eventId,
            int           timestamp
        ) : base( eventId, timestamp ) {
            this.id = id;
        }

        public DiningTableId getId() {
            return id;
        }

        public override DomainEvent fromPrimitives(
            string                     eventId, 
            int                        timestamp, 
            Dictionary<string, object> data
        ) {
            // Variables
            DiningTableDeleted domainEvent;
            // Code
            domainEvent = new DiningTableDeleted(
                new DiningTableId( data["id"].ToString() ),
                eventId,
                timestamp
            );
            return domainEvent;
        }

        public override string getEventName() {
            return "dining.table.deleted";
        }

        public override Dictionary<string, object> toPrimitives() {
            // Variables
            Dictionary<string, object> data;
            // Code
            data = new Dictionary<string, object>();
            data.Add( "id", id.getValue() );
            return data;
        }

    }

}