import sys
import datetime
from datetime import datetime
from calendar_setup import get_calendar_service

service = get_calendar_service()

def cancel_booking(id):
    service = get_calendar_service()  
    event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
        eventId=id).execute()

    event['attendees'] = []

    updated_event = service.events().update(calendarId='wtcteam19jhb@gmail.com',
        eventId=event['id'], body=event).execute()