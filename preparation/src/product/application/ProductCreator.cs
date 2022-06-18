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

    public class ProductCreator : DomainEventSubscriber<ProductCreated> {

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

        public ProductCreator( ProductRepository repository ) {
            this.repository = repository;
        }

        public async Task handleEvent( ProductCreated domainEvent ) {
            // Variables
            Product? product;
            // Code
            await Task.Run( () => {
                product = repository.findById( domainEvent.getId() );
                if( product == null ) {
                    product = Product.create(
                        id   : domainEvent.getId(),
                        name : domainEvent.getName()
                    );
                    if( !repository.save( product ) ) {
                        throw new ServerInternalErrorException();
                    }
                }
            } );
        }

    }

}