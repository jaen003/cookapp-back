/* 
 * 
 * Libraries
 *
*/

using preparation.src.restaurant.domain;
using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.diningTable.domain {

    public class DiningTableCreated : DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private DiningTableId     id;
        private DiningTableNumber number;
        private RestaurantId      restaurantId;

        /* 
         * 
         * Methods
         *
        */

        public DiningTableCreated() {
        }

        public DiningTableCreated(
            DiningTableId     id,
            DiningTableNumber number,
            RestaurantId      restaurantId
        ) {
            this.id           = id;
            this.number       = number;
            this.restaurantId = restaurantId;
        }

        public DiningTableCreated(
            DiningTableId     id,
            DiningTableNumber number,
            RestaurantId      restaurantId,
            string            eventId,
            int               timestamp
        ) : base( eventId, timestamp ) {
            this.id           = id;
            this.number       = number;
            this.restaurantId = restaurantId;
        }

        public DiningTableId getId() {
            return id;
        }

        public DiningTableNumber getNumber() {
            return number;
        }

        public RestaurantId getRestaurantId() {
            return restaurantId;
        }

        public override DomainEvent fromPrimitives(
            string                     eventId, 
            int                        timestamp, 
            Dictionary<string, object> data
        ) {
            // Variables
            DiningTableCreated domainEvent;
            // Code
            domainEvent = new DiningTableCreated(
                new DiningTableId( data["id"].ToString() ),
                new DiningTableNumber( Int32.Parse( data["number"].ToString() ) ),
                new RestaurantId( data["restaurantId"].ToString() ),
                eventId,
                timestamp
            );
            return domainEvent;
        }

        public override string getEventName() {
            return "dining.table.created";
        }

        public override Dictionary<string, object> toPrimitives() {
            // Variables
            Dictionary<string, object> data;
            // Code
            data = new Dictionary<string, object>();
            data.Add( "id", id.getValue() );
            data.Add( "number", "" + number.getValue() );
            data.Add( "restaurantId", restaurantId.getValue() );
            return data;
        }

    }

}