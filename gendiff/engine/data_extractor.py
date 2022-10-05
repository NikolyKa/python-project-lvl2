import yaml
import json


def parse_json(file_path):
    return json.load(file_path)


def parse_yaml(file_path):
    return yaml.load(file_path, Loader=yaml.Loader)


def get_content(file_path):
    return open(file_path)
