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

    public class DiningTableStatus : IntValueObject {

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

        public DiningTableStatus( int value ) : base( value ) {
        }

        public static DiningTableStatus createEnabled() {
            return new DiningTableStatus( ENABLED );
        }

        public static DiningTableStatus createDeleted() {
            return new DiningTableStatus( DELETED );
        }

    }

}