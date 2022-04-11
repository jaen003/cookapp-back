"""
 *
 * Libraries 
 *
"""

from abc      import abstractmethod
from datetime import datetime
from uuid     import uuid4

"""
 *
 * Class
 *
"""

class DomainEvent:

    """
     *
     * Attributes 
     *
    """

    __eventId   : str
    __timestamp : int

    """
     *
     * Methods 
     *
    """

    def __init__( self, eventId : str = None, timestamp : int = None ) -> object:
        if not eventId and not timestamp:
            timestamp = self.__generateTimestamp()
            eventId   = self.__generateId()
        self.__eventId   = eventId
        self.__timestamp = timestamp

    def __generateId( self ) -> str:
        return str( uuid4() )

    def __generateTimestamp( self ) -> int:
        # Variables
        timestamp : int
        now       : datetime
        # Code
        now       = datetime.now()
        timestamp = int( datetime.timestamp( now ) )
        return timestamp
    
    def getTimestamp( self ) -> int:
        return self.__timestamp
    
    def getEventId( self ) -> str:
        return self.__eventId
    
    @abstractmethod
    def getEventName( self ) -> str:
        pass
    
    @abstractmethod
    def toPrimitives( self ) -> dict[str, str | int]:
        pass

    @abstractmethod
    def fromPrimitives( self, 
        eventId   : str, 
        timestamp : int, 
        data      : dict[str, str | int]
    ) -> object:
        pass
