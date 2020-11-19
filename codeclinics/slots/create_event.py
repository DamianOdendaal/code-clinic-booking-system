import datetime
from datetime import timedelta
from calendar_setup import get_calendar_service


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


def main():
    # dates = {str((datetime.date.today() + datetime.timedelta(days=i)))[-2:]:(datetime.date.today() + datetime.timedelta(days=i)) for i in range(7)}
    dates = {}
    
    for i in range(7):
        d = datetime.date.today() + datetime.timedelta(days=i)
        dates[str(d)[-2:]] = d
    
    print('\nThese are the dates for the next 7 days:\n')
    for i in dates:
        print('\t' + i, dates[i], print_day(dates[i].weekday()+1), sep=' : ')
    
    # try:
    d = input('\nPlease choose the date of a day that you would like to volunteer on\n\n\tDate : ')
    print('\n')

    time = input('Please specify a time between 07:00-17:00 at which you will avail yourself for 30 minutes\n\n\tHH:MM : ')
    print('\n')

    start = datetime.datetime.strptime(str(dates[d])+'T'+time, '%Y-%m-%dT%H:%M').isoformat()
    # except KeyError as key_err:
    #     while True:
    #         if key_err:
    #             print('Please enter one of the available dates.')
    #             d = input('\nPlease choose the date of a day that you would like to volunteer on\n\n\tDate : ')
    #             print('\n')
    #             continue
    #         elif not key_err:
    #             break
    # except ValueError as val_err:
    #     while True:
    #         if val_err:
    #             time = input('Please specify a time between 07:00-17:00 at which you will avail yourself for 30 minutes\n\n\tHH:MM : ')
    #             print('\n')
    #             print('Please use a \':\' between the hours and minutes.\n')
    #             continue
    #         elif not val_err:
    #             break


    summary = input('Please name the concept you are offering help with\n\n\tTopic : ')
    print('\n')
    
    description = input('Please add a description of the concept you are offering help with\n\n\tDescription : ')
    print('\n')

    print('Topic :' + summary)
    print('Description :' + description)
    # print()
    print(start)


    # creates one hour event tomorrow 10 AM GMT
    service = get_calendar_service()
    
    # d = datetime.now().date()
    # tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    # start = tomorrow.isoformat()
    start_obj = datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
    end = (start_obj + timedelta(minutes=30)).isoformat()


    event_result = service.events().insert(calendarId='primary',
        body={
            "summary": summary,
            "description": description,
            "start": {"dateTime": start, "timeZone": 'Africa/Johannesburg'},
            "end": {"dateTime": end, "timeZone": 'Africa/Johannesburg'},
            
            # Adds the 'attendance UI' on the user's calendar
            # 'attendees': [{
            #   'email': 'rbrummer@student.wethinkcode.co.za'  
            # }],

            'scope': {
                # visibility property of the event
                'visibility': 'public',
                # limits the scope to a single user
                'type': 'default',
                # the email address of a user, group or domain
                'value': 'rbrummer@student.wethinkcode.co.za',
            },
            # the type of access the user receives on the events
            'role': 'reader'
        }
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

if __name__ == "__main__":
    main()