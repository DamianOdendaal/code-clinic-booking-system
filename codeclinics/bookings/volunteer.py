from calendar_setup.calendar_service import *
from bookings.processing_data import *
import sys
import re
import datetime as dt
from datetime import datetime, timedelta
from dateutil import parser
import json
from termcolor import colored


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
    # for i in range(7):
    #     date = dt.date.today() + timedelta(days=i)
    #     day = date.weekday()
    #     print(f"\t{date} {day}")

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

        if is_volunteering_valid(start, user_email):
            id = create_event(start, end, summary, description, user_email)
        else:
            print(f"\nVolunteering {fail}.")


def is_volunteering_valid(start, user_email):
    """
    This function checks if slot does not already exist and returns a boolean
    """

    data = load_data()
    
    items = []
    for item in data:
        if item[4].get('email') == user_email:
            items.append(item)

    if len(items) > 0:
        
        # Create current start and end datetime object
        start = parser.parse(start)
        end = start + timedelta(minutes=30)

        # Get new volunteer booking date and start-time in type str
        date = start.strftime("%Y-%m-%d")
        start_time = start.time()
        

        for slot in items:
            # Get existing slot end-time and date in type str
            end_time = start.time()
            date2 = parser.parse(slot[0] +" "+ slot[1]) + timedelta(minutes=30)
            end_time2 = date2.time() 

            # Condition to check if the times do not clash
            time_validation = ((end_time <= start_time and end_time < end_time2) or 
                (start_time >= end_time2 and end_time > start_time))

            
            # Condition to check if booking is on the same day and whether the times clash
            date_validation = slot[0] == date and time_validation
            if date_validation == False:
                print("\nDouble booking is not allowed!\n")
                return False

    return True


def get_date(date):
    """
    This function gets the event date in the format (YYYY-MM-DD) from the user input
    and returns a datetime object if correct or error message if not
    """

    input_date_time = input("    Enter date (YYYY-MM-DD): ")
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
    """
    This function gets the event time for the slot from the user, the time must be
    at least 30 minutes later than the current time
    """
    
    input_time = input("    Enter time (HH:MM:SS): ")
    match = re.match("\d\d:\d\d:\d\d", input_time) is None

    if match != None:
        time = parser.parse(now_date) + timedelta(hours=1)
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
    - You must book an hour before session time
    - Specify a time between 07:00-17:00
    - Make sure the time is in the format (HH:MM:SS)""")

    return error_msg
     

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
    service = get_service()

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


