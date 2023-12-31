import json

default_file_path = "./"
file_extension = ".json"

def read_dict_from_json(file_name,file_path = default_file_path):
    # Opening JSON file
    try:
        with open(file_path + file_name + file_extension, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
    except FileNotFoundError:
        return {}
    return json_object
