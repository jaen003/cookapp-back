/* 
 * 
 * Interface
 *
*/

namespace preparation.src.shared.domain {

    public interface DomainEventSubscriberBase {

        /* 
         * 
         * Methods
         *
        */

        Task handleEvent( DomainEvent domainEvent );

    }

}