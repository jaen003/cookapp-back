/* 
 * 
 * Interface
 *
*/

namespace preparation.src.shared.domain {

    public interface DomainEventsPublisher {

        /* 
         * 
         * Methods
         *
        */

        Task publish( List<DomainEvent> domainEvents );

    }

}