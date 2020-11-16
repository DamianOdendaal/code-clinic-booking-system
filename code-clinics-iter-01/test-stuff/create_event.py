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

    date_time = date_and_time_str_google()
    start_day = date_time.get('start_day')
    end_day = date_time.get('day_7')

    event_result = service.events().insert(calendarId='wtcteam19jhb@gmail.com',
        body={
            "summary": "Testing the automation",
            "description": "Automation Calendar bleeeeeeh!",
            "start": {
                "dateTime": start_day,
                "timeZone": "Africa/Johannesburg"
            },
            "end": {
                "dateTime": end_day,
                "timeZone": "Africa/Johannesburg"
            }
        }).execute()


    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
#    create_event()
    print(date_and_time_str_google())