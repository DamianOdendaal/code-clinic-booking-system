from random import randint
from calendar_setup import get_events_results, clear
from prettytable import PrettyTable
from termcolor import colored
from dateutil import parser
from bookings import *
import json
import sys
from datetime import datetime, timedelta
from dateutil import parser


def show_calendars(prompt=None):
    """
    This will get all the available slots form the WTC calendar. 
    """

    clear()
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
        data = formatted_data_output(data)
   
    for entry in data:
        table.add_row(entry)
    print(table)


def formatted_data_output(data):
    """
    This function formats the data to add color to some content when it will be
    printed out and returns the formated data
    """

    print_data = []

    if len(data[0]) == 5:
        for item in data:
            # Make the summary limited to 12 characters if it exceeds 15
            info = item[2]
            event_summary = f"{info[:12]}..." if len(info) > 15 else info
            slot = [item[0], item[1], event_summary, item[3], item[4]]

            print_data.append(slot)
            
        return print_data


    for item in data:
        # Make the summary limited to 12 characters if it exceeds that number
        info = item[2]
        event_summary = f"{info[:12]}..." if len(info) > 15 else info

        # Display just the user name instead of user email of the volunteer
        volunteer = item[4].get('email').split("@")[0]

        # Display just the user name instead of user email of the patient
        patient = item[3]
        if patient != "":
            patient = item[3].split("@")[0]
        else:
            patient = item[3]

        # Add color to the status output
        if item[6] == "[AVAILABLE]":
            status = colored("[AVAILABLE]", "cyan")
        elif item[6] == "[CONFIRMED]":
            status = colored("[CONFIRMED]", "green")

        # Return output slot
        slot = [item[0], item[1], event_summary, patient, volunteer, item[5],
                status]

        print_data.append(slot)
    
    return print_data


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
            status = "[AVAILABLE]"
            patient = ""
        elif event['status'] == 'confirmed':
            status = "[CONFIRMED]"
            patient = event['attendees'][0]['email']

        data.append([date, time, event['summary'], patient, event['creator'],
                    event['id'], status, event.get('description')])

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


def slot_details():
    """
    This function list details of the specified slot (Booking or Volunteering)
    """
    
    if len(sys.argv) != 3:
        command = ""
        for arg in sys.argv[1:]:
            command += f"{arg} "
        print(f"Unrecognized command: \"wtc-cal {command.strip()}\"")
    else:
        id = sys.argv[2].strip().upper()
        data = load_data()
    
        slot = None
        for item in data:
            if id == item[5]:
                slot = item
                break

        if slot == None:
            print(colored("Slot does not exist.", "red"))
        else:
            clear()
            print(item)
            print(len(item))
            date = parser.parse(slot[0] +" "+ slot[1]) + timedelta(minutes=30)
            end = date.strftime("%Y-%m-%d %H:%M:%S")

            msg = colored("Slot details:", "yellow")
            print(f"\n{msg} {item[5]}\n")
            print("  Creator : ", item[4].title())
            print("  Summary : ", item[3])
            print("  Description : ", "") #have to delete current data to use item[7]
            print("  Starts at : ", slot[0] + " " + slot[1])
            print("  Ends at : ", end)
            print("\n")

        