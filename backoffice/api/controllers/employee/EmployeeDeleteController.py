"""
 *
 * Libraries 
 *
"""

from flask_classful                import FlaskView
from flask_classful                import route
from src.employee.application      import EmployeeDeletor
from src.employee.infrastructure   import MysqlEmployeeRepository
from src.restaurant.infrastructure import MysqlRestaurantRepository
from src.shared.domain             import DomainEventsPublisher
from src.shared.domain             import DomainException
from src.employee.domain           import EmployeeId
from src.employee.domain           import EmployeeName
from src.employee.domain           import EmployeeEmail
from src.restaurant.domain         import RestaurantId
from flask                         import request

"""
 *
 * Class 
 *
"""

class EmployeeDeleteController( FlaskView ):

    """
     *
     * Attributes
     *
    """
    
    route_base       = '/api/v1/employee'
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
        deletor : EmployeeDeletor
        data    : dict[str, str | int]
        # Code
        data    = request.json
        deletor = EmployeeDeletor(
            repository     = MysqlEmployeeRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            deletor.delete(
                id           = EmployeeId( data.get( 'emp_id' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
