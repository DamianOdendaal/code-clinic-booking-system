import sys
import datetime
from datetime import datetime
from calendar_setup import get_calendar_service
from login import user_auth as user

if user.get_login_state():
    service = get_calendar_service()

def cancel_open_slot(id):
    """The event slot creator can delete a created slot. """

    event_result = service.events().delete(calendarId='wtcteam19jhb@gmail.com',
        eventId=id).execute()

    print("Event deleted!")


def delete_slot():
    """  """
    while True:
        if cancel_open_slot():
            break
        else:
            continue