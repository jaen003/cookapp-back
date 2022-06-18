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

    public class DiningTableNumberChanger : DomainEventSubscriber<DiningTableNumberChanged> {

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

        public DiningTableNumberChanger( DiningTableRepository repository ) {
            this.repository = repository;
        }

        public async Task handleEvent( DiningTableNumberChanged domainEvent ) {
            // Variables
            DiningTable? diningTable;
            // Code
            await Task.Run( () => {
                diningTable = repository.findById( domainEvent.getId() );
                if( diningTable == null ) {
                    throw new DiningTableNotFoundException( domainEvent.getId() );                    
                }
                diningTable.changeNumber( domainEvent.getNumber() );
                if( !repository.update( diningTable ) ) {
                    throw new ServerInternalErrorException();
                }
            } );
        }

    }

}