/* 
 * 
 * Interface
 *
*/

namespace preparation.src.product.domain {

    public interface ProductRepository {

        /* 
         * 
         * Methods
         *
        */

        bool save( Product product );

        Product? findById( ProductId id );

    }

}