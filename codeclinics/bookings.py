from calendar_setup import *
import sys
import re
import datetime as dt
from datetime import datetime, timedelta
from calendar_setup import *
from dateutil import parser
import json
from termcolor import colored


def get_user():
    """
    This function returns the user email and user name
    """

    user_details = dict
    with open(".config.json", 'r') as json_file:
        user_details = json.load(json_file)

    user_email = user_details.get('email')
    user_name = user_email.split("@")[0]

    return user_email, user_name


def cancel_booking(id):
    """
    This function cancels a booking
    """
    service = get_service() 
    event = service.events().get(calendarId='wtcteam19jhb@gmail.com', 
        eventId=id).execute()
    
    event['status'] = 'tentative'

    event['attendees'] = []

    updated_event = service.events().update(calendarId='wtcteam19jhb@gmail.com',
        eventId=event['id'], body=event).execute()


def delete_slot():
    """The event slot creator can delete a created slot. """

    event_result = service.events().delete(calendarId='wtcteam19jhb@gmail.com',
        eventId=id).execute()

    print("Event deleted!")


# def exist():
#     """
#     This checks if a booking or slot exist
#     """
#     pass


# def is_valid():
#     """
#     This function checks if a patient is allowed to cancel a booking and if a
#     volunteer is allowed to cancel a slot
#     - A patient cannot cancel another patients slot
#     - A volunteer cannot book their own slot
#     - A volunteer cannot cancel another volunteers slot
#     """
    
 




def save_data(data):
    """
    This function saves the code clinics data to a local file
    """

    old_data = load_data()

    file_path = f"{sys.path[0]}/login/data.json" 
    if data != old_data:
        with open(file_path, 'w') as file:
            json.dump(data, file)


def load_data():
    """
    This function loads the code clinics data to a local file
    """

    data = None
    file_path = f"{sys.path[0]}/login/data.json" 
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except:
        pass

    return data

