"""
 *
 * Libraries 
 *
"""

from ..valueObjects.DiningTableNumber import DiningTableNumber
from ..valueObjects.DiningTableId     import DiningTableId
from src.shared.domain                import DomainEvent

"""
 *
 * Class
 *
"""

class DiningTableNumberChanged( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id     : DiningTableId
    __number : DiningTableNumber

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : DiningTableId     = None, 
        number    : DiningTableNumber = None,
        eventId   : str               = None,
        timestamp : int               = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id     = id
        self.__number = number
    
    def getId( self ) -> DiningTableId:
        return self.__id
    
    def getNumber( self ) -> DiningTableNumber:
        return self.__number
    
    def getEventName( self ) -> str:
        return 'dining.table.number.changed'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'     : self.__id.getValue(),
            'number' : self.__number.getValue()
        }
        return data

    def fromPrimitives( self, 
        eventId   : str, 
        timestamp : int, 
        data      : dict[str, str | int]
    ) -> object:
        # Variables
        domainEvent : object
        # Code
        domainEvent = DiningTableNumberChanged(
            id        = DiningTableId( data['id'] ),
            number    = DiningTableNumber( data['number'] ),
            eventId   = eventId,
            timestamp = timestamp
        )
        return domainEvent

