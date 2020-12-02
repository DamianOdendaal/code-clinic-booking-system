from calendar_setup import get_calendar_service

service = get_calendar_service()

events_result = service.events().list(calendarId='wtcteam19jhb@gmail.com',
    maxResults=100, singleEvents=True, orderBy='startTime').execute()

events = events_result.get('items', [])

print(events['attendees'])
