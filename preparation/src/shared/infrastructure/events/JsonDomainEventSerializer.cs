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

namespace preparation.src.shared.infrastructure {

    public class JsonDomainEventSerializer { 

        /* 
         * 
         * Methods
         *
        */

        public static string serialize( DomainEvent domainEvent ) {
            // Variables
            Dictionary<string, object> data;
            string                     result;
            // Code
            data = domainEvent.toPrimitives();
            result = string.Format( 
                "{ \"id\":\"{0}\", \"name\":\"{1}\", \"timestamp\":{2}, ",
                domainEvent.getEventId(),
                domainEvent.getEventName(),
                domainEvent.getTimestamp()
            );
            result += "\"data\":{ " + string.Join( ", ", data.Select( i => 
                string.Format( "\"{0}\":\"{1}\"", i.Key, i.Value )
            ) ) + " } }";
            return result;
        }
    
    }

}