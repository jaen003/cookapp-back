"""
 *
 * Libraries 
 *
"""

from flask_classful                 import FlaskView
from flask_classful                 import route
from src.diningTable.application    import DiningTableCreator
from src.diningTable.infrastructure import MysqlDiningTableRepository
from src.restaurant.infrastructure  import MysqlRestaurantRepository
from src.shared.domain              import DomainEventsPublisher
from src.shared.domain              import DomainException
from src.diningTable.domain         import DiningTableId
from src.diningTable.domain         import DiningTableNumber
from src.diningTable.domain         import DiningTableDescription
from src.restaurant.domain          import RestaurantId
from flask                          import request

"""
 *
 * Class 
 *
"""

class EmployeePutController( FlaskView ):

    """
     *
     * Attributes
     *
    """
    
    route_base       = '/api/v1/diningTable'
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
        creator : DiningTableCreator
        data    : dict[str, str | int]
        # Code
        data    = request.json
        creator = DiningTableCreator(
            repository           = MysqlDiningTableRepository(),
            restaurantRepository = MysqlRestaurantRepository(),
            eventPublisher       = self.__eventPublisher
        )
        try:
            creator.create(
                id           = DiningTableId( data.get( 'tab_id' ) ),
                number       = DiningTableNumber( data.get( 'tab_number' ) ),
                description  = DiningTableDescription( data.get( 'tab_description' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
