/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public class RabbitmqQueueNameFormatter { 

        /* 
         * 
         * Methods
         *
        */

        public string format( DomainEventInformation eventInformation ) {
            return eventInformation.formatRabbitmqQueueName();
        }

        public string formatDeadLetter( DomainEventInformation eventInformation ) {
            return string.Format( "dead.letter.{0}", format( eventInformation ) );
        }
    
    }

}