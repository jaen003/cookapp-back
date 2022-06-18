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

namespace preparation.src.diningTable.domain {

    public class InvalidDiningTableNumberException : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_DINING_TABLE_NUMBER = 146;

        /* 
         * 
         * Methods
         *
        */

        public InvalidDiningTableNumberException( int number ) : base( 
            INVALID_DINING_TABLE_NUMBER,
            string.Format( "The dining table number {0} is invalid", number )
        ) {
        }

    }

}