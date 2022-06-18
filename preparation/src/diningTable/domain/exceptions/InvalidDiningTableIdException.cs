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

    public class InvalidDiningTableIdException : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int INVALID_DINING_TABLE_ID = 145;

        /* 
         * 
         * Methods
         *
        */

        public InvalidDiningTableIdException( string id ) : base( 
            INVALID_DINING_TABLE_ID,
            string.Format( "The dining table id {0} is invalid", id )
        ) {
        }

    }

}