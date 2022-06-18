/* 
 * 
 * Libraries
 *
*/

using preparation.src.shared.domain;

/* 
 * 
 * Class
 *
*/

namespace preparation.src.restaurant.domain {

    public class RestaurantId : UuidValueObject {

        /* 
         * 
         * Methods
         *
        */

        public RestaurantId( string value ) : base( value ) {
        }

        public RestaurantId() {
        }

    }

}