from calendar_setup import get_calendar_service
from datetime import datetime, timedelta
from pprint import pprint

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


def show_student_calendar():
    """Displaying 7 days of events from the student's calendar."""
    # Change this to using the intergrated (e.g wtc_team19_jhb) Codeclinic email

    date = date_and_time_str_google()
    events_result = service.events().list(calendarId='primary',
        timeMin=date.get('start_day'), timeMax=date.get('end_day'), 
        maxResults=100, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items')

    if not events:
        print('No upcoming events found!')

    print('Your next 7 days upcoming events:\n')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        start_date = start.split('T')[0]
        start_time_UCT = start.split('+')[0].split('T')[1]
        
        print(f"{start_date} | {start_time_UCT} | {event['summary']}")
        # start_date = start.split('T')[1]
        
        # print(f"{start} || {event['summary']}")

# if __name__ == "__main__":
#     show_student_calendar()