from calendar_setup.calendar_service import *
from ics import Calendar, Event
from icalendar import vCalAddress
import sys
import re
import datetime as dt
from datetime import datetime, timedelta
from dateutil import parser
import json
from termcolor import colored


# iCal calendar object
cal = Calendar()


def get_user():
    """
    This function returns the user email and user name
    """

    user_details = None
    config_path = f"{sys.path[0]}/files/json/.config.json"
    with open(config_path, 'r') as json_file:
        user_details = json.load(json_file)

    user_email = user_details.get('email')
    user_name = user_email.split("@")[0]

    return user_email, user_name


def cancel():
    """
    This function cancels a booking
    """
    now = datetime.now()

    if len(sys.argv) != 3:
        command = ""
        for arg in sys.argv[1:]:
            command += f"{arg} "
        print(f"\nUnrecognized command: \"wtc-cal {command.strip()}\"\n")
    else:
        data = load_data()
        id = sys.argv[2]

        slot = None
        for item in data:
            if id == item[5]:
                slot = item
                break

        if slot == None:
            print(colored("Slot does not exist.", "red"))
        else:
            user_email = get_user()[0]
            
            if user_email == slot[3]:
                delete_booking(slot, now)
            elif user_email == slot[4].get('email'):
                delete_slot(slot)
            else:
                print("Cancellation Failed")


def delete_slot(slot):
    """
    This function deletes the volunteer slot / deletes the event
    """

    service = get_service()

    if slot[3] == "-":
        id = slot[5]

        event = service.events().delete(calendarId='wtcteam19jhb@gmail.com',
        eventId=id).execute()

        print("Event cancelled!")
    else:
        print("Cancellation Failed. Patient has already booked")


def delete_booking(slot, now):
    """
    This function deletes the booked slot / deletes the booking
    """

    service = get_service()

    # Booking start time and End time
    start = parser.parse(slot[0] + " " + slot[1])
    end = start + timedelta(minutes=30)

    # Get date now and booking date
    date_now = now.date()
    date_slot = start.date()
    # print(date_now)
    # print(date_slot)

    # Get time now and booking start date 15 minutes prior
    start = start - timedelta(minutes=15)
    time_slot = start.time()
    time_now = now.time()

    # print(time_now)
    # print(time_slot)

    # Compare date and time objects
    if date_now == date_slot and time_slot <= time_now:
        print("Cannot cancel 15min befor session")
    else:
        id = slot[5]
        event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
                eventId=id).execute()

        event['status'] = 'tentative'
        event['attendees'] = []

        update_event = service.events().update(
            calendarId='wtcteam19jhb@gmail.com',
            eventId=event['id'], body=event).execute()

        print("Booking is canceled")


def save_data(data):
    """
    This function saves the code clinics data to a local file
    """

    old_data = load_data()

    file_path = f"{sys.path[0]}/files/json/data.json" 
    if data != old_data:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        # save_to_ics(data)
        # save_to_xls(data)


def load_data():
    """
    This function loads the code clinics data to a local file
    """

    data = None
    file_path = f"{sys.path[0]}/files/json/data.json" 
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # save_to_ics(data)
        # save_to_xls(data)
    except:
        pass

    return data


# def save_to_ics(data):
#     """
#     This function converts .json data file to a .ics file format and saves it
#     """

#     for e in data:
#         start = datetime.fromisoformat(e[0] + "T" + e[1] + "+02:00")
#         end = start + timedelta(minutes=30)
#         # organizer = vCalAddress(f'MAILTO:{d[4]['Email']}')

#         status = "[BOOKED]"        
#         if e[6] == "[OPEN}]":
#             status = "TENTATIVE"




        
#         event = Event()
    
#         event.add('summary', e[2])
#         event.add('dtstart', start))
#         event.add('dtend', end)
#         event.add('description', d[7])
#         event.add('organizer', )
#         event.add('STATUS', status)
#         event.add('uid', d[5])
#         if d[3] != "":
#             attendee = vCalAddress(f"MAILTO:{d[3]}")
#             event.add('attendee', attendee)
        
#         cal.events.add(event)

#     # e = Event()
#     # e.name = "My cool event"
#     # e.begin = '2014-01-01 00:00:00'
#     # c.events.add(e)
#     # c.events
#     # # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
    
#     file_path = f"{sys.path[0]}/files/ics/data.ics" 
#     with open(file_path, 'wb') as my_file:
#     #     my_file.writelines(c
#     #     ics.write(cal.to_ical())
#     # # and it's done !





   
    # with open(file_path, 'w') as file:
    #     # json.dump(data, file, indent=4)
    #     pass
    

def save_to_xls(json_path):
    """
    This function converts .json data file to a .xls file format and saves it
    """
    
    file_path = f"{sys.path[0]}/files/xls/data.xls" 
    with open(file_path, 'w') as file:
        # json.dump(data, file, indent=4)
        pass
