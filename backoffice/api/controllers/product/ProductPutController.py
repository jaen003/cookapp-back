"""
 *
 * Libraries 
 *
"""

from flask_classful                import FlaskView
from flask_classful                import route
from src.product.application       import ProductCreator
from src.product.application       import ProductRenamer
from src.product.infrastructure    import MysqlProductRepository
from src.restaurant.infrastructure import MysqlRestaurantRepository
from src.shared.domain             import DomainEventsPublisher
from src.shared.domain             import DomainException
from src.product.domain            import ProductId
from src.product.domain            import ProductName
from src.product.domain            import ProductPrice
from src.product.domain            import ProductDescription
from src.restaurant.domain         import RestaurantId
from flask                         import request
"""
 *
 * Class 
 *
"""

class ProductPutController( FlaskView ):

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

    @route( 'create', methods = ['PUT'] )
    def create( self ) -> None:
        # Variables
        creator : ProductCreator
        data    : dict[str, str | int]
        # Code
        data    = request.json
        creator = ProductCreator(
            repository           = MysqlProductRepository(),
            restaurantRepository = MysqlRestaurantRepository(),
            eventPublisher       = self.__eventPublisher
        )
        try:
            creator.create(
                id           = ProductId( data.get( 'prod_id' ) ),
                name         = ProductName( data.get( 'prod_name' ) ),
                price        = ProductPrice( data.get( 'prod_price' ) ),
                description  = ProductDescription( data.get( 'prod_description' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
    
    @route( 'rename', methods = ['PUT'] )
    def rename( self ) -> None:
        # Variables
        renamer : ProductRenamer
        data    : dict[str, str | int]
        # Code
        data    = request.json
        renamer = ProductRenamer(
            repository     = MysqlProductRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            renamer.rename(
                id           = ProductId( data.get( 'prod_id' ) ),
                name         = ProductName( data.get( 'prod_name' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400