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

    public class DiningTableDeletor : DomainEventSubscriber<DiningTableDeleted> {

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

        public DiningTableDeletor( DiningTableRepository repository ) {
            this.repository = repository;
        }

        public async Task handleEvent( DiningTableDeleted domainEvent ) {
            // Variables
            DiningTable? diningTable;
            // Code
            await Task.Run( () => {
                diningTable = repository.findById( domainEvent.getId() );
                if( diningTable == null ) {
                    throw new DiningTableNotFoundException( domainEvent.getId() );                    
                }
                diningTable.delete();
                if( !repository.update( diningTable ) ) {
                    throw new ServerInternalErrorException();
                }
            } );
        }

    }

}