"""
 *
 * Libraries 
 *
"""

from flask_classful             import FlaskView
from flask_classful             import route
from src.product.application    import ProductDeletor
from src.product.infrastructure import MysqlProductRepository
from src.shared.domain          import DomainEventsPublisher
from src.shared.domain          import DomainException
from src.product.domain         import ProductId
from src.restaurant.domain      import RestaurantId
from flask                      import request

"""
 *
 * Class 
 *
"""

class ProductDeleteController( FlaskView ):

    """
     *
     * Attributes
     *
    """
    
    route_base       = '/api/v1/product'
    __eventPublisher : DomainEventsPublisher

    """
     *
     * Methods
     *
    """
    
    def __init__( self, eventBus : DomainEventsPublisher ):
        self.__eventPublisher = eventBus

    @route( '', methods = ['DELETE'] )
    def delete( self ) -> None:
        # Variables
        deletor : ProductDeletor
        data    : dict[str, str | int]
        # Code
        data    = request.json
        deletor = ProductDeletor(
            repository     = MysqlProductRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            deletor.delete(
                id           = ProductId( data.get( 'prod_id' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
