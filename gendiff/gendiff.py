from gendiff.engine.data_extractor import get_content, parse_json, parse_yaml
from gendiff.engine.engine import collect_diff_segments
from gendiff.formaters.stylish import stylish_format
from gendiff.formaters.plain import plain_format
from gendiff.formaters.json import json_format

STYLES = {'stylish': stylish_format,
          'plain': plain_format,
          'json': json_format}


def generate_diff(first_file, second_file, format_='stylish'):
    first_dict = get_content(first_file)
    second_dict = get_content(second_file)
    if first_file.endswith('.json'):
        first_dict = parse_json(first_dict)
        second_dict = parse_json(second_dict)
    elif first_file.endswith('.yml') or first_file.endswith('.yaml'):
        first_dict = parse_yaml(first_dict)
        second_dict = parse_yaml(second_dict)
    diff = STYLES[format_](collect_diff_segments(first_dict, second_dict))
    return diff
