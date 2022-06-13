/* 
 * 
 * Interface
 *
*/

namespace preparation.src.shared.domain {

    public interface DomainEventSubscriber<T> : DomainEventSubscriberBase where T : DomainEvent {

        /* 
         * 
         * Methods
         *
        */

        async Task DomainEventSubscriberBase.handleEvent( DomainEvent domainEvent ) {
            var genericEvent = domainEvent as T;
            if( genericEvent != null ) {
                await handleEvent( genericEvent );
            }
        }

        Task handleEvent( T domainEvent );

    }

}