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

namespace preparation.src.product.domain {

    public class ProductDeleted : DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private ProductId id;

        /* 
         * 
         * Methods
         *
        */

        public ProductDeleted() {
        }

        public ProductDeleted( ProductId id ) {
            this.id = id;
        }

        public ProductDeleted(
            ProductId id,
            string    eventId,
            int       timestamp
        ) : base( eventId, timestamp ) {
            this.id = id;
        }

        public ProductId getId() {
            return id;
        }

        public override DomainEvent fromPrimitives(
            string                     eventId, 
            int                        timestamp, 
            Dictionary<string, object> data
        ) {
            // Variables
            ProductDeleted domainEvent;
            // Code
            domainEvent = new ProductDeleted(
                new ProductId( data["id"].ToString() ),
                eventId,
                timestamp
            );
            return domainEvent;
        }

        public override string getEventName() {
            return "product.deleted";
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