import json


def load_json_file(file_path):
    """
    opens the JSON configuration file and returns it.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def dump_to_json(file_path, data):
    """
    dumps the config file, with indent=2
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
