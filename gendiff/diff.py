from gendiff.engine.data_extractor import get_data
from gendiff.engine.engine import gendiff


def generate_diff(first_file, second_file, form='stylish'):
    first_dict, second_dict = get_data(first_file, second_file)
    diff = gendiff(first_dict, second_dict)
    return diff
