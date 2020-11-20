from calendar_setup import get_calendar_service
from datetime import datetime, timedelta
from tabulate import tabulate
from prettytable import PrettyTable
from termcolor import colored

# Fetching the Google Calendar API
service = get_calendar_service()

def date_and_time_str_google():
    """Converting datetime python data format into a date string that matches 
    the google time format. 

    This function returns a dictionary of date and time."""

    raw_date_min = datetime.now()
    now_split = str(raw_date_min).split(" ")
    now = now_split[0] + 'T' + now_split[1] + 'Z'

    raw_date_max = raw_date_min + timedelta(6)
    day_7_split = str(raw_date_max).split(" ")
    day_7 = day_7_split[0] + 'T' + day_7_split[1] + 'Z'

    date = {
        "start_day": now,
        "end_day": day_7
    }

    return date


def colored_headings():
    """Defining variables for the Slot Grid template."""
    
    colors = {
        "date_header": colored("DATE", 'green'),
        "time_header": colored("TIME", 'green'),
        "summary": colored("SUMMARY", 'cyan'),
        "volunteer": colored("VOLUNTEER", 'red'),
        "patient": colored("PATIENT", "magenta"),
        "etag": colored("ID", "yellow"),
        "booked": colored("[BOOKED]", "green"),
        "available": colored("[OPEN]", "cyan"),
        "canceled": colored("[CANCELED]", "red")
    }

    return colors


def show_code_clinics_calendar():
    """ """

    colors = colored_headings()
    date = date_and_time_str_google()

    events_result = service.events().list(calendarId='wtcteam19jhb@gmail.com',
        timeMin=date.get('start_day'), timeMax=date.get('end_day'),
        maxResults=100, singleEvents=True, orderBy='startTime').execute()

    events = events_result.get('items', [])

    data = []
    if not events:
        print("No upcoming events found!")

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        patient = "--"

        start_date = start.split('T')[0]
        start_time_UCT = start.split('+')[0].split('T')[1]

        data.append([start_date, start_time_UCT, event['summary'], patient, 
            event['creator'].get('email'),
            event['id']])

    return data


def get_slots_calendar():

    colors = colored_headings()
    data = show_code_clinics_calendar()

    table = PrettyTable()
    table.field_names = [colors.get("date_header"), colors.get("time_header"),
        colors.get("summary"), colors.get("patient"), colors.get("volunteer"), 
        colors.get("etag")]

    for entry in data:
        table.add_row(entry)

    print(table)


def view_student_calendar():

    colors = colored_headings()
    
    
# def show_student_calendar():
#     """Displaying 7 days of events from the student's calendar."""

#     date = date_and_time_str_google()
#     events_result = service.events().list(calendarId='wtcteam19jhb@gmail.com',
#         timeMin=date.get('start_day'), timeMax=date.get('end_day'), 
#         maxResults=100, singleEvents=True, orderBy='startTime').execute()
#     events = events_result.get('items')

#     if not events:
#         print('No upcoming events found!')

#     print('Your next 7 days upcoming events:\n')
#     for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        
        # start_date = start.split('T')[0]
        # start_time_UCT = start.split('+')[0].split('T')[1]
        
#         print(f"{start_date} | {start_time_UCT} | {event['summary']}")


if __name__ == "__main__":
    get_slots_calendar()