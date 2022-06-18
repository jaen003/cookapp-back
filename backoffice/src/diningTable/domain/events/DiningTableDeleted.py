"""
 *
 * Libraries 
 *
"""

from src.shared.domain            import DomainEvent
from ..valueObjects.DiningTableId import DiningTableId

"""
 *
 * Class
 *
"""

class DiningTableDeleted( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id : DiningTableId

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id        : DiningTableId = None,
        eventId   : str           = None,
        timestamp : int           = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id = id
    
    def getId( self ) -> DiningTableId:
        return self.__id
    
    def getEventName( self ) -> str:
        return 'dining.table.deleted'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id' : self.__id.getValue()
        }
        return data

    def fromPrimitives( self, 
        eventId   : str, 
        timestamp : int, 
        data      : dict[str, str | int]
    ) -> object:
        return DiningTableDeleted( DiningTableId( data['id'] ), eventId, timestamp )
