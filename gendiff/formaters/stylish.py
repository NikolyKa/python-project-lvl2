import json

INDENTS = {'big': '    ', 'low': ' ', '-': '  - ', '+': '  + '}


def convert(dictionary, depth):
    indent = INDENTS["big"] * depth
    result = '{\n'
    keys = dictionary.keys()
    for key in keys:
        value = dictionary.get(key)
        result += f'{indent}{INDENTS["big"]}{key}:{INDENTS["low"]}'
        result += get_values(value, depth)
    result += indent + '}\n'
    return result


def stylish_format(diff):
    depth = 0
    result = '{\n'
    keys = diff.keys()
    for key in keys:
        child = diff[key]
        result += rewrite(key, child, depth)
    result += '}'
    return result


def rewrite(key, child, depth):
    indent = INDENTS["big"] * depth
    status, value = child['status'], child['value']
    result = ''
    if status == 'nested':
        result += f'{indent}{INDENTS["big"]}{key}:{INDENTS["low"]}'
        result += '{\n'
        for k, v in value.items():
            result += rewrite(k, v, depth + 1)
        result += f'{indent}{INDENTS["big"]}'
        result += '}\n'
    elif status == 'changed':
        value1, value2 = value
        result += f'{indent}{INDENTS["-"]}{key}:'f'{INDENTS["low"]}'
        result += get_values(value1, depth)
        result += f'{indent}{INDENTS["+"]}{key}:'f'{INDENTS["low"]}'
        result += get_values(value2, depth)
    elif status == 'added':
        result = f'{indent}{INDENTS["+"]}{key}:' \
                 f'{INDENTS["low"]}'
        result += get_values(value, depth)
    elif status == 'deleted':
        result = f'{indent}{INDENTS["-"]}{key}:' \
                 f'{INDENTS["low"]}'
        result += get_values(value, depth)
    elif status == 'unchanged':
        result = f'{indent}{INDENTS["big"]}{key}:' \
                 f'{INDENTS["low"]}'
        result += get_values(value, depth)
    return result


def get_values(value, depth):
    if isinstance(value, dict):
        return convert(value, depth + 1)
    else:
        if not isinstance(value, str):
            return f'{json.dumps(value)}\n'
        else:
            return f'{value}\n'
