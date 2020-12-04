import sys
import datetime
from datetime import datetime
from calendar_setup import get_calendar_service
from login import user_auth as user
from termcolor import colored
from bookings import book_slot as attribute

if user.get_login_state():
    service = get_calendar_service()


def cancel_open_slot(id):
    """The event slot creator can delete a created slot. """

    event_result = service.events().delete(calendarId='wtcteam19jhb@gmail.com',
        eventId=id).execute()

    print("Event deleted!")


def cancel_a_slot(id):
    """This function blocks the user from deleting an event if it's already
    booked, or if the patient tries to delte the slot."""

    user_email = user.get_user_details().get('email')
    volunteer_email = attribute.get_attribute(id, 'email')
    patient_email = attribute.get_attribute(id, 'patient')
    status = attribute.get_attribute(id, 'status')

    if status == '[BOOKED]' and volunteer_email == user_email:
        print(f"Sorry, you cannot cancel a {colored('[BOOKED]', 'red')} a booked slot.")
    elif user_email == patient_email:
        print(f"Please run 'wtc-cal cancel_booking <argv (id)>' to cancel your own booking.")
    elif user_email != volunteer_email:
        print("You cannot cancel a SLOT which was not created by you!")
    else:
        cancel_open_slot(id)