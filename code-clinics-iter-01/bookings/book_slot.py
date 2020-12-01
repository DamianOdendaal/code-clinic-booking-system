import datetime
from datetime import timedelta
from calendar_setup import get_calendar_service
from login import user_auth as user
from bookings import list_calendars as cal

if user.get_login_state():
    service = get_calendar_service()


def block_volunteer():
    """ """

    email = user.get_user_details().get('email')
    print(email)

    # creator_email = cal.show_code_clinics_calendar()
    # for email_ in creator_email:
    # print("Email: ", get_item("53n4t5us90gp359utq5sgp52o4", "email"))
    # print("Date: ", get_item("53n4t5us90gp359utq5sgp52o4", "date"))
    # print("Time: ", get_item("53n4t5us90gp359utq5sgp52o4", "time"))
    # print("Summary: ", get_item("53n4t5us90gp359utq5sgp52o4", "summary"))
    # print("Patient:",get_item("53n4t5us90gp359utq5sgp52o4", "patient"))
    # print("Volunteer",get_item("53n4t5us90gp359utq5sgp52o4", "volunteer"))
    # print("Status: ", get_item("53n4t5us90gp359utq5sgp52o4", "status"))
    print(type(get_item("53n4t5us90gp359utq5sgp52o", "email")))




def get_item(id, prompt):
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
            string = slot[3]
            return string[5:19]
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

    print("Booking confirmed!")