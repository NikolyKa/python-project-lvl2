from gendiff.engine.data_extractor import get_content, parse_json, parse_yaml
from gendiff.engine.engine import collect_diff_segments
from gendiff.formaters.stylish import stylish_format
from gendiff.formaters.plain import plain_format
from gendiff.formaters.json import json_format
import os.path
STYLES = {'stylish': stylish_format,
          'plain': plain_format,
          'json': json_format}


def generate_diff(first_file, second_file, format_='stylish'):
    first_file_value = get_content(first_file)
    second_file_value = get_content(second_file)
    if os.path.splitext(first_file)[1] == '.json':
        first_dict = parse_json(first_file_value)
        second_dict = parse_json(second_file_value)
    elif os.path.splitext(first_file)[1] == '.yaml' or \
            os.path.splitext(first_file)[1] == '.yml':
        first_dict = parse_yaml(first_file_value)
        second_dict = parse_yaml(second_file_value)
    else:
        first_dict = first_file
        second_dict = second_file
    diff = STYLES[format_](collect_diff_segments(first_dict, second_dict))
    return diff
