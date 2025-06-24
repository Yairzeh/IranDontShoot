import json


def load_json_file(file_path):
    """
    opens the JSON configuration file and returns it.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def dump_to_json(file_path, data, indent=2):
    """
    dumps the config file, with indent.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=indent)


def insert_value_into_json_file(file_path, key, value, indent=2):
    """
    loads a json file, and dumps a key:value pair into it.
    """
    file = load_json_file(file_path)
    file[key] = value
    dump_to_json(file_path, file, indent)

def exit_program():
    print('\nExiting program...')
    exit()
