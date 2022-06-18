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

    public class ProductCreated : DomainEvent {

        /* 
         * 
         * Attributes
         *
        */

        private ProductId   id;
        private ProductName name;

        /* 
         * 
         * Methods
         *
        */

        public ProductCreated() {
        }

        public ProductCreated( ProductId id, ProductName name ) {
            this.id   = id;
            this.name = name;
        }

        public ProductCreated(
            ProductId   id,
            ProductName name,
            string      eventId,
            int         timestamp
        ) : base( eventId, timestamp ) {
            this.id   = id;
            this.name = name;
        }

        public ProductId getId() {
            return id;
        }

        public ProductName getName() {
            return name;
        }

        public override DomainEvent fromPrimitives(
            string                     eventId, 
            int                        timestamp, 
            Dictionary<string, object> data
        ) {
            // Variables
            ProductCreated domainEvent;
            // Code
            domainEvent = new ProductCreated(
                new ProductId( data["id"].ToString() ),
                new ProductName( data["name"].ToString() ),
                eventId,
                timestamp
            );
            return domainEvent;
        }

        public override string getEventName() {
            return "product.created";
        }

        public override Dictionary<string, object> toPrimitives() {
            // Variables
            Dictionary<string, object> data;
            // Code
            data = new Dictionary<string, object>();
            data.Add( "id", id.getValue() );
            data.Add( "name", "" + name.getValue() );
            return data;
        }

    }

}