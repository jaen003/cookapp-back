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

    public class ProductNotFoundException : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int PRODUCT_NOT_FOUND = 123;

        /* 
         * 
         * Methods
         *
        */

        public ProductNotFoundException( ProductId id ) : base( 
            PRODUCT_NOT_FOUND,
            string.Format( "The product {0} has not been found", id.getValue() )
        ) {
        }

    }

}