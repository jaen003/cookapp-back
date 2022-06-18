/* 
 * 
 * Interface
 *
*/

namespace preparation.src.diningTable.domain {

    public interface DiningTableRepository {

        /* 
         * 
         * Methods
         *
        */

        bool save( DiningTable diningTable );

        bool update( DiningTable diningTable );

        DiningTable? findById( DiningTableId id );

    }

}