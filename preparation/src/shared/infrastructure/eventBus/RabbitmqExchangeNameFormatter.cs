/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class RabbitmqExchangeNameFormatter { 

        /* 
         * 
         * Methods
         *
        */

        public string formatDeadLetter( string eventName ) {
            return string.Format( "dead.letter.{0}", eventName );
        }
    
    }

}