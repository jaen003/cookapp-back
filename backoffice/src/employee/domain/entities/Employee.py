"""
 *
 * Libraries 
 *
"""

from ..valueObjects.EmployeeName   import EmployeeName
from ..valueObjects.EmployeeEmail  import EmployeeEmail
from ..valueObjects.EmployeeId     import EmployeeId
from src.restaurant.domain         import RestaurantId
from ..valueObjects.EmployeeStatus import EmployeeStatus
from ..valueObjects.EmployeeRole   import EmployeeRole
from src.shared.domain             import AggregateRoot 
from ..events.EmployeeRoleChanged  import EmployeeRoleChanged
from ..events.EmployeeDeleted      import EmployeeDeleted
from ..events.EmployeeRenamed      import EmployeeRenamed
from ..events.EmployeeBlocked      import EmployeeBlocked

"""
 *
 * Class
 *
"""

class Employee( AggregateRoot ):

    """
     *
     * Attributes 
     *
    """

    __id           : EmployeeId
    __email        : EmployeeEmail
    __name         : EmployeeName
    __role         : EmployeeRole
    __status       : EmployeeStatus
    __restaurantId : RestaurantId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self,
        id           : EmployeeId,
        email        : EmployeeEmail,
        name         : EmployeeName,
        role         : EmployeeRole,
        status       : EmployeeStatus,
        restaurantId : RestaurantId
    ) -> None:
        super().__init__()
        self.__id           = id
        self.__email        = email
        self.__name         = name
        self.__role         = role
        self.__status       = status
        self.__restaurantId = restaurantId
    
    def getId( self ) -> EmployeeId:
        return self.__id

    def getEmail( self ) -> EmployeeEmail:
        return self.__email

    def getName( self ) -> EmployeeName:
        return self.__name
        
    def getRole( self ) -> EmployeeRole:
        return self.__role
    
    def getStatus( self ) -> EmployeeStatus:
        return self.__status

    def getRestaurantId( self ) -> RestaurantId:
        return self.__restaurantId
    
    def changeToWaiter( self ) -> None:
        if self.__role.isChef():
            self.__role = EmployeeRole.createWaiter()
            self.recordEvent( EmployeeRoleChanged( self.__id, self.__role ) )
    
    def changeToChef( self ) -> None:
        if self.__role.isWaiter():
            self.__role = EmployeeRole.createChef()
            self.recordEvent( EmployeeRoleChanged( self.__id, self.__role ) )
    
    def delete( self ) -> None:
        self.__status = EmployeeStatus.createDeleted()
        self.recordEvent( EmployeeDeleted( self.__id ) )
    
    def rename( self, newName : EmployeeName ) -> None:
        self.__name = newName
        self.recordEvent( EmployeeRenamed( self.__id, self.__name ) )
    
    def block( self ) -> None:
        self.__status = EmployeeStatus.createBlocked()
        self.recordEvent( EmployeeBlocked( self.__id ) )