from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecretes('client_secret.json', SCOPES)
creds = tools.run_flow(flow, store, flags)\
        if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '-7:00'
EVENT = {
    'summary': 'how to use nested loops',
    'start':  {'dateTime': '2020-11-28T10:00:00%s' % GMT_OFF},
    'end':    {'dateTime': '2020-11-28T10:30:00%s' % GMT_OFF}
}

e = CAL.events().insert(calendarId='primary',
        body=EVENT).execute()

print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'],encode('utf-8'),
        e['Start']['dateTime'], e['end']['dateTime']))  