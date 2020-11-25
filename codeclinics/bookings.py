import sys
import re
from datetime import datetime, timedelta
from calendar_setup import *
from dateutil import parser

def delete_event(id, scope):
    """
    """

    #if the idea exists in our data, then execute code below
    #else return string
    service = get_service()

    service.delete(calendarId="").execute()
    return f"session {ID} deleted"


def create_event(start, summary):
    """
    This function creates an event (slot), in the calendar
    """
    # end = 
    event = {   
                "status":'tenative',
                "creator": { "email": 'string' },
                'summary': summary,
                'description': description,
                'start': {
                    'dateTime': '', #pass date_time
                    'timeZone': 'Africa/Cairo',
                },
                'end': {
                    'dateTime': '', #pass date_time
                    'timeZone': 'Africa/Cairo',
                },
                'recurrence': [ 'RRULE:FREQ=DAILY;COUNT=1' ],
                'attendees': []
                # 'reminders': {
                #     'useDefault': False,
                #     'overrides': [
                #     {'method': 'email', 'minutes': 24 * 60},
                #     {'method': 'popup', 'minutes': 10},
                #     ],
                # },
                #   "attachments": [
                # {
                #     "fileUrl": string,
                #     "title": string,
                #     "mimeType": string,
                #     "iconLink": string,
                #     "fileId": string
                # }
                # ]
            }

    event = service.events().insert(calendarId='primary', body=event).execute()
    # print('Event created: %s' % (event.get('htmlLink'))

    return event


def book(tag):
    #check if tag is available for booking
    #file = open binary file, read and write
    # for data_obj in file:
    #     if data_obj["tag"] == tag:
    #         data = {"status": "open/booked/canceled",
    #                 "volunteer": "volunteer-email",
    #                 "datetime": "dt-object",
    #                 "summary": "description",
    #                 "tag": "tag"}

    #open the binary file and write to it
    #save the binary file and clos it
    msg = colored("Successfully booked for the code clinics session", "green")
    print(f"{msg}\nID:{tag}\nDate:Sometime")


def volunteer(id):
    """
    This function
    """

    if len(sys.argv) != 3:
        command = ""
        for arg in sys.argv[1:]:
            command += f"{arg} "
        print(f"Unrecognized command: \"wtc-cal {command.strip()}\"")
        print("\nUsage:\t\"wtc-cal volunteer [<args>]\"")
    else:
        msg = colored("Successfully", "green")
        color_id = colored(id, "cyan")
        start, summary = get_params()
        if is_valid(start, summary, id):
            create_event(start, summary)
        print(f"{msg} volunteered for the code clinics session! {color_id}")


def is_valid(date, time, summary, id):
    """
    This function checks if the id is allowed
    """
    return False


def get_params():
    """
    """

    dt1 = datetime.today()
    dt2 = ""
    date_objects = []


    match = re.match("\d\d\d\d-\d\d-\d\d", dt2) is None
    while match:
        dt2 = input("Enter date (YYYY-MM-DD): ")
        date_objects = [arg for arg in dt2.split("-", 2)]
        yy = date_objects[0]
        mm = date_objects[0]
        dd = date_objects[0]

        if int(yy) >= dt1.year and int(mm) >= dt1.month and int(dd) >= dt1.day:
            break 
        else:
            print("")
    print(re.match("\d\d\d\d-\d\d-\d\d", date))



def cancel(id, scope, person):
    #get data from binary file and delete it
    #file = open binary file, read and write
    # for data_obj in file:
    #     if data_obj["tag"] == tag:
    #         delete data_obj in file
    #         break
    #save and close file

    #check if its a volunteer of student who canceled
    #if volunteer canceled delete data_obj from file
    prompt = "session"
    #if student did, make slot open again
    # prompt = "booking"
    msg = colored(f"Code clinics {prompt} canceled", "green")
    print(f"{msg}\nID:{tag}\nDate:Sometime")

get_params()