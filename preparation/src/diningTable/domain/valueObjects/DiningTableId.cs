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

    public class DiningTableId : UuidValueObject {

        /* 
         * 
         * Methods
         *
        */

        public DiningTableId( string value ) : base( value ) {
            if( isEmpty() ) {
                throw new InvalidDiningTableIdException( value );
            }
        }

    }

}