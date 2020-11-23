import sys
import datetime
from datetime import timedelta
from calendar_setup import get_calendar_service
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request




if __name__ == "__main__":
    arg_list = []

    for arg in sys.argv[1:]:
        arg_list.append(arg)

    if arg_list[0] == 'cancel' and len(arg_list[1]) == 26:
        event_id = arg_list[1]
        
        service = get_calendar_service()

        event_result = service.events().delete(
            calendarId='wtcteam19jhb@gmail.com',
            eventId=event_id
        ).execute()