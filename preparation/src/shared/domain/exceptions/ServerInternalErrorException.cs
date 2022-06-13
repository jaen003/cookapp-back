/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.domain {

    public class ServerInternalErrorException : DomainException {

        /* 
         * 
         * Constants
         *
        */

        private const int SERVER_INTERNAL_ERROR = 103;

        /* 
         * 
         * Methods
         *
        */

        public ServerInternalErrorException() : base( 
            SERVER_INTERNAL_ERROR,
            "Internal server error occurred while the request was being processed" 
        ) {
        }

    }

}