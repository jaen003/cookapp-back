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

    public class ProductRenamer : DomainEventSubscriber<ProductRenamed> {

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

        public ProductRenamer( ProductRepository repository ) {
            this.repository = repository;
        }

        public async Task handleEvent( ProductRenamed domainEvent ) {
            // Variables
            Product? product;
            // Code
            await Task.Run( () => {
                product = repository.findById( domainEvent.getId() );
                if( product == null ) {
                    throw new ProductNotFoundException( domainEvent.getId() );
                }
                product.rename( domainEvent.getName() );
                if( !repository.update( product ) ) {
                    throw new ServerInternalErrorException();
                }
            } );
        }

    }

}