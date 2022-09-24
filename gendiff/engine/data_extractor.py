import yaml
import json


def parse_json(file_path):
    return json.load(file_path)


def parse_yaml(file_path):
    return yaml.load(file_path, Loader=yaml.Loader)


def get_content(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as file_:
            return parse_json(file_)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path) as file_:
            return parse_yaml(file_)
