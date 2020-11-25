"""
Come up with a better name....
This module basically carries out the functionality for commands
book, slots, volunteer and cancel.
"""
from random import randint
from calendar_setup import get_events_results
# from tabulate import tabulate
from prettytable import PrettyTable
from termcolor import colored

def get_slots():
    """
    This will get all the available slots form the WTC calendar. 
    """
    events_results = get_events_results()
    events = events_results.get('items', [])

    booked = colored("[BOOKED]", "green")
    available = colored("[OPEN]", "cyan")
    canceled = colored("[CANCELED]", "red")

    data = []
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        date, time = get_date_and_time(start)
        x = randint(1,50)
        if x % 3 == 0:
            data.append([date, time, event['summary'], event['creator'].get('email'), event['etag'], booked])
        elif x % 2 == 0:
            data.append([date, time, event['summary'], event['creator'].get('email'), event['etag'], available])
        else:
            data.append([date, time, event['summary'], event['creator'].get('email'), event['etag'], canceled])

    print_slots(data)


def print_slots(data):
    """
    This function will print out the slots
    """
    date = colored("DATE", 'green')
    time = colored("TIME", 'green')
    summary = colored("SUMMARY", 'cyan')
    volunteer = colored("VOLUNTEER", 'red')
    etag = colored("ID", "yellow")

    t = PrettyTable()
    t.field_names = [date,time, summary, volunteer, etag, "STATUS"]
    for entry in data:
        t.add_row(entry)
    # t.sortby("datetime")
    print(t)
    # print(tabulate(data, headers=[time, summary, volunteer,"STATUS"], tablefmt='grid'))


def get_date_and_time(date_time):
    """
    This function takes a datetime object and returns a seperate date and time
    strings
    """

    time = date_time.strftime("%H:%M:%S")
    date = date_time.strftime("%Y-%m-%d")

    return date, time



    

