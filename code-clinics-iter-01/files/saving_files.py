import sys
import json


file_path = f"{sys.path[0]}/files/.json-files/data.json"


def save_data(data):
    """Checking if the datafile stored in the local machine has recent data,
    if does, then update the file, if not, then don't do anything."""

    old_data = load_data()

    if data != old_data:
        with open(file_path, 'w') as write_data:
            json.dump(data, write_data)

def load_data():
    """Reading the save data.json file."""

    data = None
    
    try:
        with open(file_path, 'r') as read_data:
            data = json.load(read_data)
    except:
        pass

    return data
