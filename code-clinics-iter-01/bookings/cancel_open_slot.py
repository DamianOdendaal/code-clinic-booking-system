import sys
import datetime
from datetime import datetime
from calendar_setup import get_calendar_service

service = get_calendar_service()

def cancel_open_slot():
    """The event slot creator can delete a created slot. """

    