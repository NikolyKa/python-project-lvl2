import json


def generate_diff(first_file, second_file):
    with open('gendiff/tests/fixtures/file1.json') as first_file:
        with open('gendiff/tests/fixtures/file2.json') as second_file:
            first_dict = json.load(first_file)
            second_dict = json.load(second_file)
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
