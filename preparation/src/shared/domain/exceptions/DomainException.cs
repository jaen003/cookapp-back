/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.domain {

    public class DomainException : Exception {

        /* 
         * 
         * Attributes
         *
        */

        private int code;

        /* 
         * 
         * Methods
         *
        */

        public DomainException( int code, string message ) : base( message ) {
            this.code = code;
        }

        public int getCode() {
            return code;
        }

    }

}