import datetime
from datetime import timedelta
from calendar_setup import get_calendar_service
from login import user_auth as user

service = get_calendar_service()

def create_bookings(id):
    """Accepting an empty slot that was created by a volunteer using the ID
    as the system argument."""

    event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
        eventId=id).execute()

    event['status'] = 'confirmed'
    attendee = user.get_user_details().get('email')
    event['attendees'] = [
        {
            "email": attendee,
            "responseStatus": "accepted"
        }
    ]

    update_event = service.events().update(calendarId='wtcteam19jhb@gmail.com',
    eventId=event['id'], body=event).execute()

    print("Booking confirmed!")