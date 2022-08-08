import yaml
import json


def get_data(first_path, second_path):
    def get_content(file_path):
        if file_path.endswith('.json'):
            return json.load(open(file_path))
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.load(open(file_path), Loader=yaml.Loader)

    first_file = get_content(first_path)
    second_file = get_content(second_path)
    return first_file, second_file
