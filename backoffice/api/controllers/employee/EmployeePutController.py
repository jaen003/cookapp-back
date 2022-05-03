"""
 *
 * Libraries 
 *
"""

from flask_classful                import FlaskView
from flask_classful                import route
from src.employee.application      import EmployeeCreator
from src.employee.application      import EmployeeRoleChanger
from src.employee.application      import EmployeeRenamer
from src.employee.application      import EmployeeBlocker
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

class EmployeePutController( FlaskView ):

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

    @route( 'create/waiter', methods = ['PUT'] )
    def createWaiter( self ) -> None:
        # Variables
        creator : EmployeeCreator
        data    : dict[str, str | int]
        # Code
        data    = request.json
        creator = EmployeeCreator(
            repository           = MysqlEmployeeRepository(),
            restaurantRepository = MysqlRestaurantRepository(),
            eventPublisher       = self.__eventPublisher
        )
        try:
            creator.createWaiter(
                id           = EmployeeId( data.get( 'emp_id' ) ),
                email        = EmployeeEmail( data.get( 'emp_email' ) ),
                name         = EmployeeName( data.get( 'emp_name' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
    
    @route( 'create/chef', methods = ['PUT'] )
    def createChef( self ) -> None:
        # Variables
        creator : EmployeeCreator
        data    : dict[str, str | int]
        # Code
        data    = request.json
        creator = EmployeeCreator(
            repository           = MysqlEmployeeRepository(),
            restaurantRepository = MysqlRestaurantRepository(),
            eventPublisher       = self.__eventPublisher
        )
        try:
            creator.createChef(
                id           = EmployeeId( data.get( 'emp_id' ) ),
                email        = EmployeeEmail( data.get( 'emp_email' ) ),
                name         = EmployeeName( data.get( 'emp_name' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
    
    @route( 'changeTo/waiter', methods = ['PUT'] )
    def changeRoleToWaiter( self ) -> None:
        # Variables
        changer : EmployeeRoleChanger
        data    : dict[str, str | int]
        # Code
        data    = request.json
        changer = EmployeeRoleChanger(
            repository     = MysqlEmployeeRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            changer.changeToWaiter(
                id           = EmployeeId( data.get( 'emp_id' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
    
    @route( 'changeTo/chef', methods = ['PUT'] )
    def changeRoleToChef( self ) -> None:
        # Variables
        changer : EmployeeRoleChanger
        data    : dict[str, str | int]
        # Code
        data    = request.json
        changer = EmployeeRoleChanger(
            repository     = MysqlEmployeeRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            changer.changeToChef(
                id           = EmployeeId( data.get( 'emp_id' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
    
    @route( 'rename', methods = ['PUT'] )
    def rename( self ) -> None:
        # Variables
        renamer : EmployeeRenamer
        data    : dict[str, str | int]
        # Code
        data    = request.json
        renamer = EmployeeRenamer(
            repository     = MysqlEmployeeRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            renamer.rename(
                id           = EmployeeId( data.get( 'emp_id' ) ),
                name         = EmployeeName( data.get( 'emp_name' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
    
    @route( 'block', methods = ['PUT'] )
    def block( self ) -> None:
        # Variables
        blocker : EmployeeBlocker
        data    : dict[str, str | int]
        # Code
        data    = request.json
        blocker = EmployeeBlocker(
            repository     = MysqlEmployeeRepository(),
            eventPublisher = self.__eventPublisher
        )
        try:
            blocker.block(
                id           = EmployeeId( data.get( 'emp_id' ) ),
                restaurantId = RestaurantId( data.get( 'rest_id' ) )
            )
            return {}, 200
        except DomainException as exc:
            return { 'code' : exc.getCode() }, 400
