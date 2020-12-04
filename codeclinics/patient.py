from calendar_setup import *
from bookings import *
from termcolor import colored
from datetime import datetime, timedelta
from dateutil import parser


# is_booking()
def is_booking_valid(id):
    """
    This function checks if this booking is valid and returns a boolean
    """
    now = datetime.now()

    data = load_data()
    
    slot = None
    for item in data:
        if id == item[5]:
            slot = item
            break

    if slot == None:
        print(colored("Slot does not exist.", "red"))
        return False
    else:
        user_email = get_user()[0]
        date = parser.parse(slot[0] + " " + slot[1]) - timedelta(minutes=30)
        if slot[4] == user_email:
            print(colored("Volunteer cannot book their own slot.", "red"))
            return False
        elif date < now:
            print(colored("Cannot book 30 min before session.", "red"))
            return False
        elif slot[3] != "":
            print(colored("Slot is already booked.", "red"))
            return False         

    return True


def book():
    """
    This function books a volunteer slot if its available
    """
    service = get_service()
    
    if len(sys.argv) != 3:
        command = ""
        for arg in sys.argv[1:]:
            command += f"{arg} "
        print(f"\nUnrecognized command: \"wtc-cal {command.strip()}\"\n")
    else:
        id = sys.argv[2]
        if is_booking_valid(id):

            event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
            maxAttendees = 1, eventId=id).execute()

            event['status'] = 'confirmed'
            attendee = get_user()[0]
            event['attendees'] = [
                {
                    "email": attendee,
                }
            ]

            update_event = service.events().update(
                calendarId='wtcteam19jhb@gmail.com',
                eventId=event["id"], body=event).execute()

            print({colored("Booking confirmed!", "green")})