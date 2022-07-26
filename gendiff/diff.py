import json
import yaml


def open_files(first_path, second_path):
    def open_file(file_path):
        if file_path.endswith('.json'):
            return json.load(open(file_path))
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.load(open(file_path), Loader=yaml.Loader)

    first_file = open_file(first_path)
    second_file = open_file(second_path)
    return first_file, second_file


def generate_diff(first_file, second_file):
    first_dict, second_dict = open_files(first_file, second_file)
    result = '{\n'
    sorted_pairs = sorted(first_dict | second_dict)
    for key in sorted_pairs:
        prefix = ''
        if key in first_dict:
            prefix = '-'
            if second_dict.get(key) == first_dict.get(key):
                prefix = ' '
            result += f'{prefix} {key}: {first_dict[key]}\n'
        if key in second_dict and prefix != ' ':
            prefix = '+'
            result += f'{prefix} {key}: {second_dict[key]}\n'
    result += '}'
    return result
