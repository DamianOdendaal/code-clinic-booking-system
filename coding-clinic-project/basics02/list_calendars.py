from calendar_setup import get_calendar_service
import datetime
import json
from pprint import pprint


def list_calendars():
    """
    """
    service = get_calendar_service()

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])

    # pprint(events_result)
    # with open("data_file.json", "w") as write_data:
    #     json.dump(events_result, write_data)
    print(events_result)

if __name__ == "__main__":
    list_calendars()