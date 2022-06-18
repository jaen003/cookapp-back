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

    public class ProductId : UuidValueObject {

        /* 
         * 
         * Methods
         *
        */

        public ProductId( string value ) : base( value ) {
        }

    }

}