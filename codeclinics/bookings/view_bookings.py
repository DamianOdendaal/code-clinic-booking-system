from os import path
from calendar_setup import get_calendar_service
from datetime import datetime
from termcolor import colored
import sys
import os
import json

service = get_calendar_service()

def get_slots():
    """
    This will get all the available slots form the WTC calendar. 
    """
    #possibly returns all slots booked and open
    pass

def open_slots():
    """
    view open slots
    """
    pass



def get_open_slots():
    """
    view your slots
    """

    pass
print(service)