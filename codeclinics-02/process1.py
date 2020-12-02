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

# Calling the Google Calendar API
events_results = get_events_results()
events = events_results.get('items', [])


def get_date_and_time():
    """Get time and date from Google Calendar API. It has to look more readable."""


def colored_headings():
    """Defining variables for the Slot Grid template."""
    
    colors = {
        "date_header": colored("DATE", 'green'),
        "time_header": colored("TIME", 'yellow'),
        "summary": colored("SUMMARY", 'cyan'),
        "volunteer": colored("VOLUNTEER", 'red'),
        "etag": colored("ID", "yellow"),
        "booked": colored("[BOOKED]", "green"),
        "available": colored("[OPEN]", "cyan"),
        "canceled": colored("[CANCELED]", "red")
    }

    return colors


def adding_data_to_the_table():
    """Adding data to a list that will include data from the patient's API."""

    colors = colored_headings()

    data = []
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        date = start.split('T')[0]
        time = start.split('+')[0].split('T')[1]
        x = randint(1,50)
        if x % 3 == 0:
            data.append([date, time, event['summary'], 
                event['creator'].get('email'),
                event['etag'], colors.get("booked")])

        elif x % 2 == 0:
            data.append([date, time, event['summary'], 
                event['creator'].get('email'),
                event['etag'], colors.get("available")])
            
        else:
            data.append([date, time, event['summary'], 
                event['creator'].get('email'),
                event['etag'], colors.get("canceled")])

    return data

def get_slots():
    # Must use free/busy to query for open slots
    # Return events for the current 7 days
    # If 'attendees' >= 1, the event is booked
    #max 20 slots a day given that each slot is 30 mins long and are available from 8am to 18pm

    colors = colored_headings()
    
    data = adding_data_to_the_table()
        

    table = PrettyTable()
    table.field_names = [colors.get("date_header"), colors.get("time_header"), 
        colors.get("summary"), colors.get("volunteer"), colors.get("etag"), 
        "STATUS"]
        
    for entry in data:
        table.add_row(entry)

    print(table)


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
