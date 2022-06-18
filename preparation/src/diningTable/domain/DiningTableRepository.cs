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

        DiningTable? findById( DiningTableId id );

    }

}