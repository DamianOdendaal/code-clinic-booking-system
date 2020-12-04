import sys
import re
import json
import datetime as dt
from termcolor import colored
from dateutil import parser
from calendar_setup import *
from bookings import list_calendars as data
from datetime import datetime, timedelta

config_path = f"{sys.path[0]}/.config.json"

service = get_calendar_service()

def get_user():
    """
    This function returns the user email and user name
    """

    user_details = dict
    with open(config_path, 'r') as json_file:
        user_details = json.load(json_file)

    user_email = user_details.get('email')
    user_name = user_email.split("@")[0]

    return user_email, user_name


def weekdays(day):
    """Printing out days of the week, and returning a dictionary with days of
    the week."""

    week_days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    return week_days[day]


def get_date(date):
    """This function gets the event date in the format (YYYY-MM-DD) from the
    user input and returns a datetime object if correct input was inputted."""

    input_date_time = input("   Enter date (YYYY-MM-DD): ")
    match = re.match("\d\d\d\d-\d\d-\d\d", input_date_time) is None

    if match != None:
        date_now = parser.parse(date)
        input_date = parser.parse(input_date_time)
        result = (input_date - date_now).days

        if result >= 0 and result <= 30:
           return input_date
    
    date_max = (parser.parse(date) + timedelta(days=30)).strftime("%Y-%m-%d")
    error_msg = (f"""\nInvalid input error.
    - Make sure the date is in the format (YYYY-MM-DD)
    - Make sure the date is between the ({date}) and ({date_max})""")
    
    return error_msg


def get_time(result_date, now_date):
    """This function gets the event time for the slot from the user, the time 
    must be at least 30 minutes later than the current time. Also, checking if
    the time input is between 7amto 16h30 in the afternoon for booking."""
    
    input_time = input("    Enter time (HH:MM:SS): ")
    match = re.match("\d\d:\d\d:\d\d", input_time) is None

    if match != None:
        time = parser.parse(now_date) + timedelta(minutes=30)
        input_date = parser.parse(now_date.split(" ",1)[0] + " " + input_time)
        input_time = parser.parse(input_time)

        time_valid = input_time >= time
        date_valid = result_date.date() > time.date()
        date_valid2 = result_date.date() < (time + timedelta(days=7)).date()
        result = (time_valid or date_valid) and date_valid2
        time_min = dt.time(7,0,0)
        time_max = dt.time(16,30,0)
        valid = input_time.time() >= time_min and input_time.time() <= time_max

        if result and valid:
            return input_time

    error_msg = (f"""\nInvalid input error.
    - You can only book 30 min from the current time
    - Specify a time between 07:00-17:00
    - Make sure the time is in the format (HH:MM:SS)""")

    return error_msg


def is_valid(start, summary, id):
    """
    This function checks if slot does not already exist
    """
    if summary == None or start == None:
        return False
    else:
        #must check if it already exists
        # probably use the data file (manipulation) to validate this
        pass

    return True


def get_summary_and_description():
    """
    This function gets the event summary from the user
    """

    summary = input("\n\n    Enter topic: ")
    if summary != "":
        description = input("    Enter description: ")
        if description != "":
            return summary, description

    return None, None


def get_params():
    """
    This function gets the parameters (datetime and summary) needed to create
    a slot and returns a tuple of them
    """

    summary, description = get_summary_and_description()
    now = datetime.now()
    date = get_date(now.strftime("%Y-%m-%d"))
    if type(date) != datetime:
        print(date)
        return None, None, None, None

    time = get_time(date, now.strftime("%Y-%m-%d %H:%M:%S"))
    if type(time) != datetime:
        print(time)
        return None, None, None, None
    
    if type(summary) == None:
        print("Invalid input error.\n\tSummary cannot be empty")
        return None, None, None, None

    if type(description) == None:
        print("Invalid input error.\n\tDescription cannot be empty")
        return None, None, None, None
    
    start = date.strftime("%Y-%m-%d") + "T" + time.strftime("%H:%M:%S+02:00")

    end = parser.parse(start) + timedelta(minutes=30)
    end = end.strftime("%Y-%m-%dT%H:%M:%S+02:00")

    return start, end, summary, description


def create_event(start, end, summary, description, email):
    """
    This function creates an event (slot), in the calendar and returns the 
    event id
    """
    # service = get_service()

    event_result = service.events().insert(calendarId='wtcteam19jhb@gmail.com',
        body={
            "summary": summary,
            "description": description,
            "start": {
                "dateTime": start,
                "timeZone": "Africa/Johannesburg"
            },
            "end": {
                "dateTime": end,
                "timeZone": "Africa/Johannesburg"
            },
            "status": 'tentative',
            "creator": { "email": email },

        }).execute()

    msg = colored("Created [OPEN] volunteer slot", "cyan")
    print(f"\n\n{msg}\n")
    print("\tCreator :\t", email)
    print("\t[OPEN] slot ID :", event_result['id'])
    print("\tSummary :\t", event_result['summary'])
    print("\tDescription :\t", event_result['description'])
    print("\tStarts at :\t", event_result['start']['dateTime'])
    print("\tEnds at :\t", event_result['end']['dateTime'])
    print("\n")

    return event_result['id']


def volunteer():
    """
    This function creates a volunteering slot
    """

    user_email, user_name = get_user()
    print(colored(f"{user_name.title()} slot volunteering:", "cyan"))

    dates = {}

    for i in range(7):
        day = dt.date.today() + timedelta(days=i)
        dates[str(day)[-2:]] = day


    print('\nThese are the dates for the next 7 days:\n')
    for i in dates:
        print('\t' + i, dates[i], weekdays(dates[i].weekday()+1), sep=' : ')


    if len(sys.argv) != 2:
        command = ""
        for arg in sys.argv[1:]:
            command += f"{arg} "
        print(f"Unrecognized command: \"wtc-cal {command.strip()}\"")
        print("\nUsage:\t\"wtc-cal volunteer [<args>]\"")
    else:
        fail = colored("Failed", "red")
        start, end, summary, description = get_params()
        if is_valid(start, summary, user_email):
            id = create_event(start, end, summary, description, user_email)
            id = colored(id.upper(), "cyan")
        else:
            print(f"\nVolunteering {fail}.")