import yaml
import json


def get_content(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as file_:
            return json.load(file_)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path) as file_:
            return yaml.load(file_, Loader=yaml.Loader)
