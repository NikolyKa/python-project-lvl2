import yaml
import json


def parse_json(file_content):
    return json.loads(file_content)


def parse_yaml(file_content):
    return yaml.load(file_content, Loader=yaml.Loader)


def get_content(file_path):
    with open(file_path) as file:
        return file.read()
