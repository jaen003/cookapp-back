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

    public class DiningTableNotFoundException : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int DINING_TABLE_NOT_FOUND = 148;

        /* 
         * 
         * Methods
         *
        */

        public DiningTableNotFoundException( DiningTableId id ) : base( 
            DINING_TABLE_NOT_FOUND,
            string.Format( "The dining table {0} has not been found", id.getValue() )
        ) {
        }

    }

}