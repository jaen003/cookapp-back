
"""
 *
 * Libraries 
 *
"""

import json
from typing                   import Any
from src.shared.domain        import DomainEvent
from injector                 import inject
from .DomainEventsInformation import DomainEventsInformation
from .DomainEventInformation  import DomainEventInformation

"""
 *
 * Class
 *
"""

class JsonDomainEventDeserializer:

    """
     *
     * Attributes 
     *
    """

    __eventsInformation : DomainEventsInformation

    """
     *
     * Methods 
     *
    """

    @inject
    def __init__( self, eventsInformation : DomainEventsInformation ) -> object:
        self.__eventsInformation = eventsInformation

    def deserialize( self, messageBody : str ) -> DomainEvent:
        # Variables
        messageData      : dict[str, Any]
        eventClass       : type
        eventName        : str
        domainEvent      : DomainEvent
        eventInformation : DomainEventInformation
        # Code
        messageData      = json.loads( messageBody )
        eventName        = messageData['name']
        eventInformation = self.__eventsInformation.findByEventName( eventName )
        eventClass       = eventInformation.getEventClass()
        domainEvent      = eventClass()
        domainEvent = domainEvent.fromPrimitives(
            eventId   = messageData['id'],
            timestamp = messageData['timestamp'],
            data      = messageData['data']
        )
        return domainEvent