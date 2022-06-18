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

    public class ProductStatus : IntValueObject {

        /* 
         * 
         * Constants
         *
        */

        private const int ENABLED = 1;
        private const int DELETED = 2;

        /* 
         * 
         * Methods
         *
        */

        public ProductStatus( int value ) : base( value ) {
        }

        public static ProductStatus createEnabled() {
            return new ProductStatus( ENABLED );
        }

        public static ProductStatus createDeleted() {
            return new ProductStatus( DELETED );
        }

    }

}