from datetime import datetime, timedelta
from calendar_setup import get_calendar_service


def main():
    # creates one hour event tomorrow 10 AM GMT
    service = get_calendar_service()


    d = datetime.now()#.date()

    summary = input('Please name the concept you are offering help with: ')
    description = input('Please describe the concept you are offering help with: ')
    start = input('Please specify a time between 08:00-16:00\n at which you can avail yourself for 30 minutes\n like this HH:MM : ')
    start = datetime.strptime(start, '%H:%M')
    # end = str(int(start) + 30)


    # d.hour = start

    # print(d)
    # print(d.year)
    # print(d.month)
    # print(d.day)
    # print(d.hour)
    # print(d.minute)
    
    # tomorrow = datetime(d.year, d.month, d.day, d.hour, d.minute, 10)
    # tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    # start = tomorrow.isoformat()
    # end = (tomorrow + timedelta(minutes=30)).isoformat()

    print(start)
    print(end)

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
                'visibility': 'default',
                # limits the scope to a single user
                'type': 'user',
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