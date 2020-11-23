"""
Come up with a better name....
This module basically carries out the functionality for commands
book, slots, volunteer and cancel.
"""
from random import randint
from bookings.calendar_setup import get_events_results
from tabulate import tabulate
from prettytable import PrettyTable
from termcolor import colored
from datetime import datetime, timedelta
import json
# Calling the Google Calendar API
service = get_events_results()
events_results = service.events().list(calendarId='primary').execute()

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

def date_and_time_str_google():
    """Converting datetime python data format into a date string that matches 
    the google time format. 
    This function returns a dictionary of date and time."""

    raw_date_min = datetime.now()
    now_split = str(raw_date_min).split(" ")
    now = now_split[0] + 'T' + now_split[1] + 'Z'

    raw_date_max = raw_date_min + timedelta(6)
    day_7_split = str(raw_date_max).split(" ")
    day_7 = day_7_split[0] + 'T' + day_7_split[1] + 'Z'

    date = {
        "start_day": now,
        "end_day": day_7
    }

    return date


def adding_data_to_the_table():
    """Adding data to a list that will include data from the patient's API."""

    colors = colored_headings()
    date = date_and_time_str_google()

    data = []
    print(events)
    if not events:
        print('No upcoming events found.')   
  
    writing_to_json_file(events)     
   
    if not events:
        print("No upcoming events found!")

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        patient = "--"

        start_date = start.split('T')[0]
        start_time_UCT = start.split('+')[0].split('T')[1]

        data.append([start_date, start_time_UCT, event['summary'], patient, 
            event['creator'].get('email'),
            event['id']])

    return data

def writing_to_json_file(user_details):
    """Writing user data to a hidden .config file."""

  

    with open('bookings/.slotsdata.json', 'w') as write_config:
        json.dump(user_details, write_config)

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
