
from calendar_setup import get_calendar_service
from datetime import datetime, timedelta
from tabulate import tabulate
from prettytable import PrettyTable
from termcolor import colored

from login import user_auth as user

if user.get_login_state():
   service = get_calendar_service() 
# Fetching the Google Calendar API

def date_and_time_str_google():
    """Converting datetime python data format into a date string that matches 
    the google time format. 
    This function returns a dictionary of date and time."""

    #service = get_calendar_service()
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
    #service = get_calendar_service()
    colors = {
        "date_header": colored("DATE", 'green'),
        "time_header": colored("TIME", 'yellow'),
        "summary": colored("SUMMARY", 'cyan'),
        "volunteer": colored("VOLUNTEER", 'red'),
        "etag": colored("ID", "yellow"),
        "booked": colored("[BOOKED]", "red"),
        "available": colored("[OPEN]", "cyan"),
        "canceled": colored("[CANCELED]", "red"),
        'status': colored('STATUS', 'green'),
        "patient": colored("PATIENT", "magenta")
    }

    return colors


def show_code_clinics_calendar():
    """This function shows the calendar for Code Clinic Calendar. This calendar
    is global, and can be seen by every WeThinkCode_ student. It returns a list
    of date, time, meeting summary, the patient email (booked), the volunteer
    email and the meeting ID."""
    #service = get_calendar_service()
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

        #print(event)

        if event['status'] == 'tentative':
            status = colors.get('available')
            patient = colored('[AVAILABLE]', 'green')
        elif event['status'] == 'confirmed':
            status = colors.get('booked')
            patient = event['attendees'][0]['email']

        start_date = start.split('T')[0]
        start_time_UCT = start.split('+')[0].split('T')[1]

        data.append([start_date, start_time_UCT, event['summary'], patient, 
            event['creator'].get('email'), status, event['id']])

    return data


#def save_volunteer_id


def show_student_calendar():
    """This function shows the personal student calendar. It's only visible to
    the logged in student alone. It returns a list of the date, time, the 
    meeting topic, the creator email and the meeting ID. """
    #service = get_calendar_service()
    colors = colored_headings()
    date = date_and_time_str_google()

    events_result = service.events().list(calendarId='primary',
        timeMin=date.get('start_day'), timeMax=date.get('end_day'),
        maxResults=100, singleEvents=True, orderBy='startTime').execute()

    events = events_result.get('items', [])

    student_calendar = []
    if not events:
        print("No upcoming events found!")

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))

        start_date = start.split('T')[0]
        start_time_UCT = start.split('+')[0].split('T')[1]

        student_calendar.append([start_date, start_time_UCT, event['summary'],
            event['creator'].get('email'), event['id']])

    return student_calendar


def get_student_calendar():
    """It displays the data of the student in a table form.
    > Prints out 7 days of content to the terminal."""
    #service = get_calendar_service()
    colors = colored_headings()
    data = show_student_calendar()

    table = PrettyTable()
    table.field_names = ["DATE", "TIME",
        "SUMMARY", "CREATOR", "ID"]

    for entry in data:
        table.add_row(entry)

    print(table)


def get_slots_calendar():
    """It displays the data of the Code Clinic Calendar in a table form.
    > Prints out 7 days of calendar content to the terminal."""
    #service = get_calendar_service()
    colors = colored_headings()
    data = show_code_clinics_calendar()

    table = PrettyTable()
    table.field_names = [colors.get("date_header"), colors.get("time_header"),
        colors.get("summary"), colors.get("patient"), colors.get("volunteer"), 
        colors.get('status'), colors.get("etag")]

    for entry in data:
        table.add_row(entry)

    print(table)

# import datetime
# from calendar_setup import get_calendar_service




# def student_cal():
    
#     service = get_calendar_service()

#     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#     print('Getting the upcoming 7 events')
#     events_result = service.events().list(calendarId='primary', timeMin=now,
#                                         maxResults=7, singleEvents=True,
#                                         orderBy='startTime').execute()
#     events = events_result.get('items', [])

#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])


# def wtc_clinic_cal():

#     service = get_calendar_service()

#     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#     print('Getting the upcoming 7 slots')
#     slots_result = service.events().list(calendarId='wtcteam19jhb@gmail.com', timeMin=now,
#                                         maxResults=7, singleEvents=True,
#                                         orderBy='startTime').execute()
#     slots = slots_result.get('items', [])

#     if not slots:
#         print('No slot found.')
#     for slot in slots:
#         start = slot['start'].get('dateTime', slot['start'].get('date'))
#         print(start, slot['summary'])


# if __name__ == "__main__":
#     student_cal()
#     wtc_clinic_cal()
