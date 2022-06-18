/* 
 * 
 * Libraries
 *
*/

using preparation.src.diningTable.domain;
using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.diningTable.application {

    public class DiningTableCreator : DomainEventSubscriber<DiningTableCreated> {

        /* 
         * 
         * Attributes
         *
        */

        private DiningTableRepository repository;

        /* 
         * 
         * Methods
         *
        */

        public DiningTableCreator( DiningTableRepository repository ) {
            this.repository = repository;
        }

        public async Task handleEvent( DiningTableCreated domainEvent ) {
            // Variables
            DiningTable? diningTable;
            // Code
            await Task.Run( () => {
                diningTable = repository.findById( domainEvent.getId() );
                if( diningTable == null ) {
                    diningTable = DiningTable.create(
                        id           : domainEvent.getId(),
                        number       : domainEvent.getNumber(),
                        restaurantId : domainEvent.getRestaurantId()
                    );
                    if( !repository.save( diningTable ) ) {
                        throw new ServerInternalErrorException();
                    }
                }
            } );
        }

    }

}