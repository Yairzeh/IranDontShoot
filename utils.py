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


def load_and_dump_to_json(file_path, key, value, indent=2):
    """
    loads the config file, and dumps the key:value pair into it.
    """
    file = load_json_file(file_path)
    file[key] = value
    dump_to_json(file_path, file, indent)
