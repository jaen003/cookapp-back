/* 
 * 
 * Class
 *
*/

namespace preparation.src.product.domain {

    public class Product {

        /* 
         * 
         * Attributes
         *
        */

        private ProductId     id;
        private ProductName   name;
        private ProductStatus status;

        /* 
         * 
         * Methods
         *
        */

        public Product( 
            ProductId     id,
            ProductName   name,
            ProductStatus status
        ) {
            this.id     = id;
            this.name   = name;
            this.status = status;
        }

        public ProductId getId() {
            return id;
        }

        public ProductName getName() {
            return name;
        }

        public ProductStatus getStatus() {
            return status;
        }

        public static Product create( ProductId id, ProductName name ) {
            return new Product(
                id     : id,
                name   : name,
                status : ProductStatus.createEnabled()
            );
        }

        public void rename( ProductName newName ) {
            name = newName;
        }

        public void delete() {
            status = ProductStatus.createDeleted();
        }

    }

}