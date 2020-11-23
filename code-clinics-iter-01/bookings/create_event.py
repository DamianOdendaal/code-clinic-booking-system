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


def get_user_event_input():
    """Prompting the user (volunteer) to enter the date and time they'll like to
    add the slot to the calendar."""

    dates = {}

    for i in range(7):
        day = datetime.date.today() + datetime.timedelta(days=i)
        dates[str(day)[-2:]] = day

    try:
        dt = input('\nPlease choose the date of a day that you would like to volunteer on\n\n\tDate : ')
        print('\n')
        time = input('Please specify a time between 07:00-17:00 at which you will avail yourself for 30 minutes\n\n\tHH:MM : ')
        print('\n')
        summary = input('Please name the concept you are offering help with\n\n\tTopic : ')
        print('\n')
        description = input('Please add a description of the concept you are offering help with\n\n\tDescription : ')
        print('\n')

        start = datetime.datetime.strptime(str(dates[dt])+'T'+time, '%Y-%m-%dT%H:%M').isoformat()
        start_event = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
        end = (start_event + timedelta(minutes=30)).isoformat()        

        event_result = service.events().insert(calendarId='wtcteam19jhb@gmail.com',
            body={
                "summary": "Created an Event",
                "description": "Automation Calendar bleeeeeeh!",
                "start": {
                    "dateTime": start,
                    "timeZone": "Africa/Johannesburg"
                },
                "end": {
                    "dateTime": end,
                    "timeZone": "Africa/Johannesburg"
                }
            }).execute()

        events_creator = service.events().list(calendarId='primary').execute()
        creator = events_creator.get('summary')

        print("Created [OPEN] volunteer slot\n")
        print("\tCreator :\t", creator)
        print("\t[OPEN] slot ID :", event_result['id'])
        print("\tSummary :\t", event_result['summary'])
        print("\tDescription :\t", event_result['description'])
        print("\tStarts at :\t", event_result['start']['dateTime'])
        print("\tEnds at :\t", event_result['end']['dateTime'])

        return True

    except KeyError:
        print('>>> Please select 1 of the available dates of the next 7 days.')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        return False

    except ValueError:
        print('>>> Please use a \':\' (colon) between your chosen time\'s hours and minutes.')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        return False


def get_user_input():
    """  """

def create_event():
    """A function that creates an event in the Google Calendar using the sys
    argument value."""

    date_time = date_and_time_str_google()
    start_day = date_time.get('start_day')
    end_day = date_time.get('day_7')

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId='wtcteam19jhb@gmail.com',
        body={
            "summary": "Created an Event",
            "description": "Automation Calendar bleeeeeeh!",
            "start": {
                "dateTime": start,
                "timeZone": "Africa/Johannesburg"
            },
            "end": {
                "dateTime": end,
                "timeZone": "Africa/Johannesburg"
            }
        }).execute()



    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


def test():
    events_result = service.events().list(calendarId='primary').execute()
    events = events_result.get('items', [])

    # pprint(events)
    print(events.get('organizer'))

if __name__ == '__main__':
    test()