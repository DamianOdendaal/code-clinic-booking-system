import datetime
from datetime import timedelta
from calendar_setup import get_calendar_service
from login import user_auth as user
from termcolor import colored
from bookings import list_calendars as cal

if user.get_login_state():
    service = get_calendar_service()


def block_volunteer():
#     """ """

#     print(email)
    clinic = cal.show_code_clinics_calendar()
    # for i in clinic:
    #     print(i)
#     creator_email = cal.show_code_clinics_calendar()
#     # for email_ in creator_email:
    print("Email: ", get_attribute("53n4t5us90gp359utq5sgp52o4", "email"))
    print("Date: ", get_attribute("53n4t5us90gp359utq5sgp52o4", "date"))
    print("Time: ", get_attribute("53n4t5us90gp359utq5sgp52o4", "time"))
    print("Summary: ", get_attribute("53n4t5us90gp359utq5sgp52o4", "summary"))
    print("Patient:",get_attribute("53n4t5us90gp359utq5sgp52o4", "patient"))
    print("Volunteer",get_attribute("53n4t5us90gp359utq5sgp52o4", "volunteer"))
    print(f"Status: {get_attribute('53n4t5us90gp359utq5sgp52o4', 'patient')}")
    




def get_attribute(id, prompt):
    """
    This function access the volunteer and patient items
    """
    calendar = cal.show_code_clinics_calendar()

    slot = None
    for item in calendar:
        if item[6] == id:
            slot = item
    if slot != None:
        if prompt == "email":
            return slot[4]
        elif prompt == "date":
            return slot[0]
        elif prompt == "time":
            return slot[1]
        elif prompt == "summary":
            return slot[2]
        elif prompt == "patient":
            #use regex later stage things
            return slot[3]
        elif prompt == "volunteer":
            return slot[4]
        elif prompt == "status":
            string = slot[5]
            return string[5:13] 
    
    return slot


def create_bookings(id):
    """Accepting an empty slot that was created by a volunteer using the ID
    as the system argument."""

    event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
        maxAttendees = 1, eventId=id).execute()

    event['status'] = 'confirmed'
    attendee = user.get_user_details().get('email')
    event['attendees'] = [
        {
            "email": attendee,
        }
    ]


    update_event = service.events().update(calendarId='wtcteam19jhb@gmail.com',
    eventId=event['id'], body=event).execute()

    print("BOOKING CONFIRMED!")
    booking_summary(id)


def confirm_bookings(id):
    """Validation function that prevents the volunteer from booking their own
    slot."""

    user_email = user.get_user_details().get('email')
    volunteer_email = get_attribute(id, 'email')
    patient_email = get_attribute(id, 'patient')
    status = get_attribute(id, 'status')

    if user_email == volunteer_email:
        print("A volunteer cannot book an their OWN slot!")
    elif status == '[BOOKED]':
        print(f"Sorry, the event is already booked by {patient_email}.")
        print(f"Please check an open slot. {colored('[AVAILABLE]', 'green')}")
    else:
        create_bookings(id)


def booking_summary(id):
    """This will print out the booking details in a summarised format."""

    volunteer_email = get_attribute(id, 'email')
    help_topic = get_attribute(id, 'summary')
    time = get_attribute(id, 'time')
    date = get_attribute(id, 'date')

    print("Booking Summary:")
    print(f"You're getting help with: {help_topic}")
    print(f"The volunteer: {volunteer_email}")
    print(f"Time: {time}")
    print(f"Date: {date}")