from os import path
from calendar_setup import get_events_results
from datetime import datetime, timedelta
from termcolor import colored
import sys
import os
import json


def get_time_date():
    """Getting the current time and date. This function returns a dictionary
    of time and date."""

    now = datetime.now()
    date = now.strftime("%D")
    time = now.strftime("%H:%M")

    date_and_time = {
        "date": date,
        "time": time
    }

    return date_and_time


def get_user_details():
    """Retrieving user details from the calendar setup module."""

    events_results = get_events_results()
    
    user_email = events_results.get('summary')
    username = user_email.split('@')[0]
    date_and_time = get_time_date()

    user_details = {
        "username": username,
        "email": user_email,
        "date": date_and_time['date'],
        "time": date_and_time['time']
    }

    return user_details


def remove_token():
    """ Removing the token file if the user is not logged in or if the token
    file exists.""" 

    not_error = False
    # user_details = get_user_details()

    token_path = f"{sys.path[0]}/token.pickle"
    current_login_path = f"{sys.path[0]}/current_login.txt"
    
    try:
        os.remove(token_path)
        os.remove(current_login_path)
    except FileNotFoundError:
        not_error = False
        print("You already loggged out!")
        print("\nPlease run: \"wtc-cal login\"\n")

    
    # if not path.exists(token_path):
    #     with open('.config.json','w') as write_config:
    #         json.dump(user_details, write_config)

    return not_error


def validate_email(user_email):
    """Ths function checks if used email is in the WeThinkCode_ organization.
    It should check if the domain contains '@student.wethinkcode.co.za' for 
    students or '@wethinkcode.co.za' for the staff."""

    user_name = user_email.split('@')[0]
    domain_name = user_email.split('@')[1]

    if domain_name.find("wethinkcode.co.za") > -1:
        print(f'Welcome {str(user_name).capitalize()}.')
    else:
        os.remove(path.realpath('token.pickle'))
        print("Invalid email address!")


def writing_to_json_file(user_details):
    """Writing user data to a hidden .config file."""

    user_details = get_user_details()

    with open('.config.json', 'w') as write_config:
        json.dump(user_details, write_config)


def writing_to_a_txt(current_user):
    """ Writing the current user email address to a .txt file"""

    user_file_txt = get_user_details()
    current_user = user_file_txt.get('email')

    with open('current_login.txt', 'w') as current_login:
        current_login.write(current_user)


def get_user_status():
    """Getting the status of the signed in user. If they're signed in, it should
    print out that the user is logged in, if not, then it should instructions to
    the user about loggin in."""
    
    token_path = f"{sys.path[0]}/token.pickle"
    if path.exists(token_path):
        user_email = ""
        with open("current_login.txt", 'r') as f:
            user_email = f.readline()

        connected = colored('[CONNECTED]', 'green')
        print(connected + " Google Calendar | Code Clinic Booking System") 
        print(f"Signed in as {user_email}")
    else:
        offline = colored('[OFFLINE]', 'red')
        print(offline + "\nPlease run: \"wtc-cal login\"")


def user_login():
    """Signing the user by redirecting them to the sign in page. If they are
    logged in, print out a statemet. If they're not, create a token file for
    them."""

    remove_token()
    
    user_details = get_user_details()
    user_email = user_details.get("email")

    token_path = f"{sys.path[0]}/token.pickle"
    if not path.exists(token_path):
        validate_email(user_email)
        writing_to_json_file(user_details)
        writing_to_a_txt(user_email)
    else:
        print("You are already logged in!")


def user_logout():
    """Loggin out the user from the booking sysem."""

    if remove_token():
        print("You have been logged out from the system!")


time_out = datetime.now() + timedelta(minutes=30)
def auto_logout():
    """
    This function checks if your token is still valid
    """
    if datetime.now() >= time_out:
        user_logout()
        print("\nToken expired:\nPlease login using \"wtc-cal login\"")
