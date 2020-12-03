from calendar_setup import *
from bookings import *


def is_valid():
    """
    This function checks if this booking is allowed by the user
    """
    return True


def book(id):
    """
    This function books a volunteer slot if its available
    """
    
    if is_valid():
        cal_id = 'wtcteam19jhb@gmail.com'
        event = service.events().get(calendarId=cal_id, 
        maxAttendees = 1, eventId=id).execute()


        event['status'] = 'confirmed'
        attendee = get_user()[0]
        event['attendees'] = [
            {
                "email": attendee,
            }
        ]

        update_ev = service.events().update(calendarId=cal_id,
                    eventId=event["id"], body=event).execute()

        print(f"Booking {colored("confirmed!", "green")}")