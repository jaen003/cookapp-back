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

    public class InvalidProductNameException : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_PRODUCT_NAME = 124;

        /* 
         * 
         * Methods
         *
        */

        public InvalidProductNameException( string name ) : base( 
            INVALID_PRODUCT_NAME,
            string.Format( "The product name {0} is invalid", name )
        ) {
        }

    }

}