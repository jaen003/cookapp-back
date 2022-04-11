"""
 *
 * Libraries 
 *
"""

import json
from typing            import Any
from src.shared.domain import DomainEvent

"""
 *
 * Class
 *
"""

class JsonDomainEventSerializer:

    """
     *
     * Methods 
     *
    """

    @classmethod
    def serialize( cls, domainEvent : DomainEvent ) -> str:
        # Variables
        messageData : dict[str, Any]
        # Code
        messageData = {
            'id'        : domainEvent.getEventId(),
            'name'      : domainEvent.getEventName(),
            'timestamp' : domainEvent.getTimestamp(),
            'data'      : domainEvent.toPrimitives()
        }
        return json.dumps( messageData )