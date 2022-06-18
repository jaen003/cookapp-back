/* 
 * 
 * Libraries
 *
*/

using preparation.src.restaurant.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.diningTable.domain {

    public class DiningTable {

        /* 
         * 
         * Attributes
         *
        */

        private DiningTableId     id;
        private DiningTableNumber number;
        private RestaurantId      restaurantId;
        private DiningTableStatus status;

        /* 
         * 
         * Methods
         *
        */

        public DiningTable( 
            DiningTableId     id,
            DiningTableNumber number,
            DiningTableStatus status,
            RestaurantId      restaurantId
        ) {
            this.id           = id;
            this.number       = number;
            this.status       = status;
            this.restaurantId = restaurantId;
        }

        public DiningTableId getId() {
            return id;
        }

        public DiningTableNumber getNumber() {
            return number;
        }

        public RestaurantId getRestaurantId() {
            return restaurantId;
        }

        public DiningTableStatus getStatus() {
            return status;
        }

        public static DiningTable create( 
            DiningTableId     id,
            DiningTableNumber number,
            RestaurantId      restaurantId
        ) {
            return new DiningTable(
                id           : id,
                number       : number,
                status       : DiningTableStatus.createEnabled(),
                restaurantId : restaurantId
            );
        }

        public void delete() {
            status = DiningTableStatus.createDeleted();
        }

        public void changeNumber( DiningTableNumber newNumber ) {
            number = newNumber;
        }

    }

}