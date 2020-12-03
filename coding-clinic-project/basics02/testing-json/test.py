import json

data = {
    "president": {
        "name": "Cyril Ramaphosa",
        "race": "black"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)