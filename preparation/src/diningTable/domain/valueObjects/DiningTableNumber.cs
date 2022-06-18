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

    public class DiningTableNumber : IntValueObject {

        /* 
         * 
         * Constants
         *
        */

        private const int MINIMUN_NUMBER = 1;
        private const int MAXIMUM_NUMBER = 255;

        /* 
         * 
         * Methods
         *
        */

        public DiningTableNumber( int value ) : base( value ) {
            if( !isValid() ) {
                throw new InvalidDiningTableNumberException( value );
            }
        }

        private bool isValid() {
            return isGreaterThanOrEqual( new IntValueObject( MINIMUN_NUMBER ) ) &&
                isLessThanOrEqual( new IntValueObject( MAXIMUM_NUMBER ) );
        }

    }

}