from gendiff.engine.data_extractor import get_content
from gendiff.engine.engine import collect_diff_segments
from gendiff.formaters.stylish import stylish_format
from gendiff.formaters.plain import plain_format
from gendiff.formaters.json import json_format

styles = {'stylish': stylish_format,
          'plain': plain_format,
          'json': json_format}


def generate_diff(first_file, second_file, form='stylish'):
    first_dict = get_content(first_file)
    second_dict = get_content(second_file)
    diff = styles[form](collect_diff_segments(first_dict, second_dict))
    return diff
