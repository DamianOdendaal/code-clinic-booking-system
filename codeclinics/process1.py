"""
Come up with a better name....
This module basically carries out the functionality for commands
book, slots, volunteer and cancel.
"""
from random import randint
from calendar_setup import get_events_results
from tabulate import tabulate
from prettytable import PrettyTable
from termcolor import colored

def get_slots():
    # Must use free/busy to query for open slots
    # Return events for the current 7 days
    # If 'attendees' >= 1, the event is booked
    #max 20 slots a day given that each slot is 30 mins long and are available from 8am to 18pm

    """
    This will get all the available slots form the WTC calendar. 
    """
    events_results = get_events_results()

    events = events_results.get('items', [])
    datetime = colored("TIME", 'green')
    summary = colored("SUMMARY", 'cyan')
    volunteer = colored("VOLUNTEER", 'red')
    etag = colored("ID", "yellow")
    booked = colored("[BOOKED]", "green")
    available = colored("[OPEN]", "cyan")
    canceled = colored("[CANCELED]", "red")

    data = []
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        x = randint(1,50)
        if x % 3 == 0:
            data.append([start, event['summary'], event['creator'].get('email'), event['etag'], booked])
        elif x % 2 == 0:
            data.append([start, event['summary'], event['creator'].get('email'), event['etag'], available])
        else:
            data.append([start, event['summary'], event['creator'].get('email'), event['etag'], canceled])
        

    t = PrettyTable()
    t.field_names = [datetime, summary, volunteer, etag, "STATUS"]
    for entry in data:
        t.add_row(entry)
    # t.sortby("datetime")
    print(t)
    # print(tabulate(data, headers=[time, summary, volunteer], tablefmt='textile'))


def book_event(tag):
    #check if tag is available for booking
    #file = open binary file, read and write
    # for data_obj in file:
    #     if data_obj["tag"] == tag:
    #         data = {"status": "open/booked/canceled",
    #                 "volunteer": "volunteer-email",
    #                 "datetime": "dt-object",
    #                 "summary": "description",
    #                 "tag": "tag"}

    #open the binary file and write to it
    #save the binary file and clos it
    msg = colored("Successfully booked for the code clinics session", "green")
    print(f"{msg}\nID:{tag}\nDate:Sometime")
    

def volunteer(tag):
    #if tag exists in events create data_obj in a binary data file
    # data = {"status": "open/booked/canceled",
    #         "volunteer": "volunteer-email",
    #         "datetime": "dt-object",
    #         "summary": "description",
    #         "tag": "tag"}
    msg = colored("Successfully volunteered for the code clinics session", "green")
    print(f"{msg}\nID:{tag}\nDate:Sometime")


def cancel(tag,person):
    #get data from binary file and delete it
    #file = open binary file, read and write
    # for data_obj in file:
    #     if data_obj["tag"] == tag:
    #         delete data_obj in file
    #         break
    #save and close file

    #check if its a volunteer of student who canceled
    #if volunteer canceled delete data_obj from file
    prompt = "session"
    #if student did, make slot open again
    # prompt = "booking"
    msg = colored(f"Code clinics {prompt} canceled", "green")
    print(f"{msg}\nID:{tag}\nDate:Sometime")
