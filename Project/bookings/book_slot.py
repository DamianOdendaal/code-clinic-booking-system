
import datetime
from datetime import timedelta
from calendar_setup import get_calendar_service
from login import user_auth as user


# def student_accept_yes(attendee):
#     """When a student accepts a booking, the program automatically accepts
#     and RSVP the event."""

#     event = service.events().get(calendarId=attendee, eventId=id).execute()
#     event['attendees'] = [
#         {
#             'responseStatus': 'accepted'
#         }
#     ]

def create_bookings(id):
    """Accepting an empty slot that was created by a volunteer using the ID
    as the system argument."""

    service = get_calendar_service()
    event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
        maxAttendees = 1, eventId=id).execute()

    event['status'] = 'confirmed'
    attendee = user.get_user_details().get('email')
    event['attendees'] = [
        {
            "email": attendee,
            # "responseStatus": 'accepted'
        }
    ]

    # student_accept_yes(attendee)

    update_event = service.events().update(calendarId='wtcteam19jhb@gmail.com',
    eventId=event['id'], body=event).execute()

    print("Booking confirmed!")