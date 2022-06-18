/* 
 * 
 * Libraries
 *
*/

using preparation.src.product.domain;
using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.product.application {

    public class ProductDeletor : DomainEventSubscriber<ProductDeleted> {

        /* 
         * 
         * Attributes
         *
        */

        private ProductRepository repository;

        /* 
         * 
         * Methods
         *
        */

        public ProductDeletor( ProductRepository repository ) {
            this.repository = repository;
        }

        public async Task handleEvent( ProductDeleted domainEvent ) {
            // Variables
            Product? product;
            // Code
            await Task.Run( () => {
                product = repository.findById( domainEvent.getId() );
                if( product == null ) {
                    throw new ProductNotFoundException( domainEvent.getId() );
                }
                product.delete();
                if( !repository.update( product ) ) {
                    throw new ServerInternalErrorException();
                }
            } );
        }

    }

}