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

    public class InvalidProductIdException : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_PRODUCT_ID = 109;

        /* 
         * 
         * Methods
         *
        */

        public InvalidProductIdException( string id ) : base( 
            INVALID_PRODUCT_ID,
            string.Format( "The product id {0} is invalid", id )
        ) {
        }

    }

}