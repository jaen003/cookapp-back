/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.domain {

    public class StringValueObject {

        /* 
         * 
         * Attributes
         *
        */

        private string value;

        /* 
         * 
         * Methods
         *
        */

        public StringValueObject( string value ) {
            this.value = value;
        }

        public string getValue() {
            return value;
        }

        public bool isEmpty() {
            return value == string.Empty;
        }

        public bool equals( StringValueObject other ) {
            return value == other.getValue();
        }

        public bool isLongerThan( StringValueObject other ) {
            return value.Length > other.getValue().Length;
        }

        public bool isLongerThanOrEqual( StringValueObject other ) {
            return value.Length >= other.getValue().Length;
        }

    }

}