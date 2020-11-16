import sys
import os
from os import path
import quickstart
import json
from datetime import datetime


def user_login():
    try:
        os.remove(path.realpath("token.pickle"))
    except FileNotFoundError:
        pass

    
    if not path.exists("token.pickle"):
        user_email = quickstart.start_login()
        user_name = user_email.split("@")[0]
        date_time = get_time_date()
        user_details = {
                    "Username": user_name,
                    "Email": user_email,
                    "Date": date_time['date'],
                    "Time": date_time['time']       
                }

        validate(user_email)
    
        with open('.config.json','w') as write_config:
            json.dump(user_details, write_config)

        f = open("current_login.txt",'w')
        f.write(user_email)
        f.close()
    else:
        print('Your logged in already') 
       

def user_logout():
    os.remove(path.abspath("token.pickle"))
    print("You have logged out.")

     
def status():
    
    if path.exists("token.pickle"):
        f = open("current_login.txt",'r')
        user_email = f.readline()
        f.close()       
        print(f"[CONNECTED] Google Calendar | Code Clinics\nSigned in as: {user_email}")
    else:
        print("[OFFLINE]\nPlease run: \"wtc-cal login\"")


def get_time_date():
    now = datetime.now()
    date = now.strftime("%D")
    time = now.strftime("%H:%M")    
    
    date_and_time = {
        "date": date,
        "time": time
    }

    return date_and_time


def validate(user_email):
    #We should probably use regex if more funcitonality (distinct matches) is needed



    user_name = user_email.split("@")[0]
    expression = user_email.split("@")[1]

    if expression.find("wethinkcode.co.za") > -1:
        print('Welcome ' + str(user_name))
    else:
        # os.remove(path.abspath("token.pickle"))
        os.remove(path.realpath("token.pickle"))
        print("Invalid login details!")


"""
Add a function to revoke authorisation after 30 mins has lapsed.
"""





              