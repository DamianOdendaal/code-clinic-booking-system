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


def create_event():
    """A function that creates an event in the Google Calendar using the sys
    argument value."""

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    start = tomorrow.isoformat() + 'Z'
    end = (tomorrow + timedelta(hours=1)).isoformat() + 'Z'

    event_result = service.events().insert(calendarId='wtcteam19jhb@gmail.com',
        body={
            "summary": "Testing the automation",
            "description": "Automation Calendar bleeeeeeh!",
            "start": {
                "dateTime": start,
                "timeZone": "Africa/Johannesburg"
            },
            "end": {
                "dateTime": end,
                "timeZone": "Africa/Johannesburg"
            },
            "attendees": [
                {
                    "email": 'tetema@student.wethinkcode.co.za'
                }
            ]
        }).execute()


    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
    create_event()
    # print(date_and_time_str_google())