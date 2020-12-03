from random import randint
from calendar_setup import get_events_results
from prettytable import PrettyTable
from termcolor import colored
from dateutil import parser
from bookings import get_user
import json
import sys


def show_calendars(prompt=None):
    """
    This will get all the available slots form the WTC calendar. 
    """
    
    if prompt == "primary":
        user_name = get_user()[1] 
        print(f"\n{user_name.title()} Calendar")
        print_slots(get_primary_calendar())
    else:
        print("\nCode Clinics Calendar")
        print_slots(get_code_clinics_calendar())


def print_slots(data):
    """
    This function will print out the slots
    """

    date = colored("DATE", 'green')
    time = colored("TIME", 'green')
    summary = colored("SUMMARY", 'cyan')
    volunteer = colored("VOLUNTEER", 'red')
    creator = colored("CREATOR", 'red')
    patient = colored("PATIENT", "magenta")
    id = colored("ID", "yellow")

    table = PrettyTable()

    if len(data[0]) == 5:
        table.field_names = [date, time, summary, creator, id]
    else:
        table.field_names = [date, time, summary, patient, 
                            volunteer, id, "STATUS"]
   
    for entry in data:
        table.add_row(entry)
    print(table)


def get_date_and_time(date_time):
    """
    This function takes a datetime object and returns a seperate date and time
    strings
    """
    date_time = parser.parse(date_time)
    time = date_time.strftime("%H:%M:%S")
    date = date_time.strftime("%Y-%m-%d")

    return date, time

    
def get_code_clinics_calendar():
    """
    This function returns the code-clinics calendar
    """

    events_results = get_events_results('wtcteam19jhb@gmail.com')
    events = events_results.get('items', [])

    data = []
    if not events:
        print('No upcoming events found.')
    
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        date, time = get_date_and_time(start)

        if event['status'] == 'tentative':
            status = colored("[AVAILABLE]", "cyan")
            patient = colored('-', 'magenta')
        elif event['status'] == 'confirmed':
            status = colored("[CONFIRMED]", "green")
            patient = event['attendees'][0]['email']

        info = event['summary']
        summary = info[:12] if len(event['summary']) > 12 else info
        volunteer = event['creator'].get('email').split("@")[0]

        data.append([date, time, summary, patient.split("@")[0], 
                volunteer, event['id'].upper(), status])

    return data


def get_primary_calendar():
    """
    This function returns the primary calendar (user calendar)
    """

    events_results = get_events_results()
    events = events_results.get('items', [])

    data = []
    if not events:
        print('No upcoming events found.')

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        date, time = get_date_and_time(start)

        data.append([date, time, event['summary'],
                    event['creator'].get('email'), event['id'].upper()])

    return data


#WAITING ON DATAFILE
def slot_details(id):
    """
    This function list details of the specified slot (Booking or Volunteering)
    """
    pass


def save_data():
    """
    This function saves the code clinics data to a local file
    """

    current_data = get_code_clinics_calendar()
    old_data = load_data()

    file_path = f"{sys.path[0]}/login/data.json" 
    if current_data != old_data:
        with open(file_path, 'w') as file:
            json.dump(current_data, file)
    

def load_data():
    """
    This function loads the code clinics data to a local file
    """

    data = None
    file_path = f"{sys.path[0]}/login/data.json" 
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except:
        pass

    return data