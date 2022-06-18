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

    public class DiningTableNumberChanged : DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private DiningTableId     id;
        private DiningTableNumber number;

        /* 
         * 
         * Methods
         *
        */

        public DiningTableNumberChanged() {
        }

        public DiningTableNumberChanged(
            DiningTableId     id,
            DiningTableNumber number
        ) {
            this.id     = id;
            this.number = number;
        }

        public DiningTableNumberChanged(
            DiningTableId     id,
            DiningTableNumber number,
            string            eventId,
            int               timestamp
        ) : base( eventId, timestamp ) {
            this.id     = id;
            this.number = number;
        }

        public DiningTableId getId() {
            return id;
        }

        public DiningTableNumber getNumber() {
            return number;
        }

        public override DomainEvent fromPrimitives(
            string                     eventId, 
            int                        timestamp, 
            Dictionary<string, object> data
        ) {
            // Variables
            DiningTableNumberChanged domainEvent;
            // Code
            domainEvent = new DiningTableNumberChanged(
                new DiningTableId( data["id"].ToString() ),
                new DiningTableNumber( Int32.Parse( data["number"].ToString() ) ),
                eventId,
                timestamp
            );
            return domainEvent;
        }

        public override string getEventName() {
            return "dining.table.number.changed";
        }

        public override Dictionary<string, object> toPrimitives() {
            // Variables
            Dictionary<string, object> data;
            // Code
            data = new Dictionary<string, object>();
            data.Add( "id", id.getValue() );
            data.Add( "number", "" + number.getValue() );
            return data;
        }

    }

}