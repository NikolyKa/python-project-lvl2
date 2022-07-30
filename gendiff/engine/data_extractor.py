import pathlib
from pathlib import Path
import yaml
import json
path_json = Path('gendiff','tests','fixtures','json')
path_yaml = Path('gendiff','tests','fixtures','yaml/')
print(path_json)
def get_data(first_path, second_path):
    def get_content(file_path):
        path_json = Path('gendiff', 'tests', 'fixtures', 'json', file_path)
        path_yaml = Path('gendiff', 'tests', 'fixtures', 'yaml/', file_path)
        if file_path.endswith('.json'):
            return json.load(open(path_json))
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.load(open(path_yaml), Loader=yaml.Loader)

    first_file = get_content(first_path)
    second_file = get_content(second_path)
    return first_file, second_file
