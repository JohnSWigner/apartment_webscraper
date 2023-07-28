import json

file_path = "../"
file_extension = ".json"

def write_dict_to_json(file_name, data):
    # Serializing json
    json_object = json.dumps(data, indent=4)

    # Writing to sample.json
    with open(file_path + file_name + file_extension, "w") as outfile:
        outfile.write(json_object)