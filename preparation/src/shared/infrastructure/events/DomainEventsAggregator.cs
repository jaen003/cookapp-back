/* 
 * 
 * Class
 *
*/

namespace preparation.src.shared.infrastructure {

    public static class DomainEventsAggregator {

        /* 
         * 
         * Methods
         *
        */

        public static IServiceCollection addDomainEvents( this IServiceCollection services ) {
            // Variables
            List<DomainEventInformation> eventsInformation;
            List<Type>                   eventSubscriberClasses;
            List<Type>                   eventClasses;
            // Code
            eventsInformation = new List<DomainEventInformation>();
            eventClasses      = DomainEventsLocator.locate();
            foreach( Type eventClass in eventClasses ) {                
                eventSubscriberClasses = DomainEventSubscribersLocator.locate( eventClass );
                eventsInformation.Add( new DomainEventInformation( 
                    eventClass, 
                    eventSubscriberClasses 
                ) );                
                foreach( Type eventSubscriberClass in eventSubscriberClasses ) {
                    services.AddTransient( eventSubscriberClass, eventSubscriberClass );
                }
            }
            services.AddTransient( s => new DomainEventsInformation( eventsInformation ) );
            return services;
        }

    }
}
