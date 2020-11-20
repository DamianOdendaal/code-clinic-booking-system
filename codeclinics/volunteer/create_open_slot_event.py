import datetime
from datetime import timedelta
from calendar_setup import get_calendar_service
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def print_day(day):
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
    
    """
    Still need to handle for SATURDAYS & SUNDAYS.
    Still need to handle for times before 07:00 & after 17:00.
    """
    
    # dates = {str((datetime.date.today() + datetime.timedelta(days=i)))[-2:]:(datetime.date.today() + datetime.timedelta(days=i)) for i in range(7)}
    dates = {}
    
    for i in range(7):
        d = datetime.date.today() + datetime.timedelta(days=i)
        dates[str(d)[-2:]] = d

    print('\nThese are the dates for the next 7 days:\n')
    for i in dates:
        print('\t' + i, dates[i], print_day(dates[i].weekday()+1), sep=' : ')

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

        service = get_calendar_service()

        event_result = service.events().insert(calendarId='primary',
            body={
                "summary": summary,
                "description": description,
                "start": {"dateTime": start, "timeZone": 'Africa/Johannesburg'},
                "end": {"dateTime": end, "timeZone": 'Africa/Johannesburg'},
                "scope": {
                    # visibility property of the event
                    "visibility": "public",
                    # limits the scope to a single user
                    "type": "default",
                    # the email address of a user, group or domain
                    "value": "rbrummer@student.wethinkcode.co.za",
                },
                # the type of access the user receives on the events
                'role': 'reader'
            }
        ).execute()

        # 'summary' in this scope is used as event titles.
        # This is just to get 'summary' as the event creator's email address.
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


def main():
    while True:
        if get_user_event_input():
            break
        else:
            continue


if __name__ == "__main__":
    main()