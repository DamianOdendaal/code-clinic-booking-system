from cal_setup import get_calendar_service

def main():
    service = get_calendar_service()

    # call the Calendar API
    print('Getting a list of calendars')
    calendar_result = service.calendarList().list().execute()

    calendars = calendar_result.get('items', [])
    
    if not calendars:
        print('No calendars found.')
    
    for calendar in calendars:
        print(calendar['summary'])

if __name__ == "__main__":
    main()