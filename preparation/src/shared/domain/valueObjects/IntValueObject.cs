/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.domain {

    public class IntValueObject {

        /* 
         * 
         * Attributes
         *
        */

        private int value;

        /* 
         * 
         * Methods
         *
        */

        public IntValueObject( int value ) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }

        public bool equals( IntValueObject other ) {
            return value == other.getValue();
        }

        public bool isLessThan( IntValueObject other ) {
            return value < other.getValue();
        }

        public bool isGreaterThan( IntValueObject other ) {
            return value > other.getValue();
        }

        public bool isLessThanOrEqual( IntValueObject other ) {
            return value <= other.getValue();
        }

        public bool isGreaterThanOrEqual( IntValueObject other ) {
            return value >= other.getValue();
        }

        public string toString() {
            return value.ToString();
        }

    }

}