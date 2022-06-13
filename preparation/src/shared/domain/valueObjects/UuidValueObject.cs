/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.domain {

    public class UuidValueObject {

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

        public UuidValueObject( string value ) {
            this.value = value;
        }

        public UuidValueObject() {
            value = generateValue();
        }

        private string generateValue() {
            return Guid.NewGuid().ToString();
        }

        public string getValue() {
            return value;
        }

        public bool isEmpty() {
            return value == string.Empty;
        }

        public bool equals( UuidValueObject other ) {
            return value == other.getValue();
        }

    }

}