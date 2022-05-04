"""
 *
 * Libraries 
 *
"""

from flask_classful                 import FlaskView
from flask_classful                 import route
from src.diningTable.application    import DiningTableDeletor
from src.diningTable.infrastructure import MysqlDiningTableRepository
from src.shared.domain              import DomainEventsPublisher
from src.shared.domain              import DomainException
from src.diningTable.domain         import DiningTableId
from src.restaurant.domain          import RestaurantId
from flask                          import request

"""
 *
 * Class 
 *
"""

class DiningTableDeleteController( FlaskView ):

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

    @route( '', methods = ['DELETE'] )
    def createWaiter( self ) -> None:
        # Variables
        deletor : DiningTableDeletor
        data    : dict[str, str | int]
        # Code
        data    = request.json
        deletor = DiningTableDeletor(
            repository     = MysqlDiningTableRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            deletor.delete(
                id           = DiningTableId( data.get( 'tab_id' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
