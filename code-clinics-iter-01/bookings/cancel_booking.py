import sys
import datetime
from datetime import datetime
from calendar_setup import get_calendar_service
from termcolor import colored
from login import user_auth as user
from bookings import book_slot as attribute


if user.get_login_state():
    service = get_calendar_service()


def cancel_booking(id):
    """This function makes the attendees list empty and changes the event status
    to tentative, thus, removing the user from the booking and making the slot
    empty."""

    service = get_calendar_service()  
    event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
        eventId=id).execute()
    
    event['status'] = 'tentative'

    event['attendees'] = []

    updated_event = service.events().update(calendarId='wtcteam19jhb@gmail.com',
        eventId=event['id'], body=event).execute()


def cancel_user_booking(id):
    """This function only works when the user cancel their own book."""

    user_email = user.get_user_details().get('email')
    volunteer_email = attribute.get_attribute(id, 'email')
    patient_email = attribute.get_attribute(id, 'patient')
    status = attribute.get_attribute(id, 'status')
    available  = colored('[AVAILABLE]', 'red')

    if status == '[AVAILABLE]':
        print(f"You cannot cancel a slot which is not booked -  {available}")
    elif status == '[BOOKED]' and user_email != patient_email:
        print("You cannot cancel another student's booking.")
        print("Please cancel your own booking!")
    else:
        cancel_booking(id)