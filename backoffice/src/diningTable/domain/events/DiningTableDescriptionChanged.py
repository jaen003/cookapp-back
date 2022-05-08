"""
 *
 * Libraries 
 *
"""

from ..valueObjects.DiningTableDescription import DiningTableDescription
from ..valueObjects.DiningTableId          import DiningTableId
from src.shared.domain                     import DomainEvent

"""
 *
 * Class
 *
"""

class DiningTableDescriptionChanged( DomainEvent ):

    """
     *
     * Attributes 
     *
    """

    __id          : DiningTableId
    __description : DiningTableDescription

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        id          : DiningTableId          = None,
        description : DiningTableDescription = None,
        eventId     : str                    = None,
        timestamp   : int                    = None
    ) -> None:
        super().__init__( eventId, timestamp )
        self.__id          = id
        self.__description = description
    
    def getId( self ) -> DiningTableId:
        return self.__id
    
    def getDescription( self ) -> DiningTableDescription:
        return self.__description
    
    def getEventName( self ) -> str:
        return 'dining.table.description.changed'
    
    def toPrimitives( self ) -> dict[str, str | int]:
        # Variables
        data : dict[str, str | int]
        # Code
        data = {
            'id'          : self.__id.getValue(),
            'description' : self.__description.getValue()
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
        domainEvent = DiningTableDescriptionChanged(
            id          = DiningTableId( data['id'] ),
            description = DiningTableDescription( data['description'] ),
            eventId     = eventId,
            timestamp   = timestamp
        )
        return domainEvent

