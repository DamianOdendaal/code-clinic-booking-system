from cal_setup import get_calendar_service
from pprint import pprint
import datetime

def get_current_time():
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M")

    return now

def main():
    service = get_calendar_service()

    # Call the google Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print("Getting a list of events")

    events_result = service.events().list(calendarId='primary', timeMin=now, 
        maxResults=10, singleEvents=True, orderBy='startTime').execute()

    events = events_result.get('items', [])
    print(events_result.get('timeZone'))
    

    if not events:
        print('No upcoming events found!')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == "__main__":
    main()