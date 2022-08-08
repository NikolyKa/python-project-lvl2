from gendiff.engine.data_extractor import get_data
from gendiff.engine.engine import collect_diff_segments
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
styles = {'stylish': stylish,
          'plain': plain}


def generate_diff(first_file, second_file, form='stylish'):
    first_dict, second_dict = get_data(first_file, second_file)
    diff = styles[form](collect_diff_segments(first_dict, second_dict))
    return diff
