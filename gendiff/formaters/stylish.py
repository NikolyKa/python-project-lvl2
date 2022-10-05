import json

INDENTS = {'big': '    ', 'low': ' ', '-': '  - ', '+': '  + '}


def convert(dictionary, depth):
    indent = INDENTS["big"] * depth
    res = '{\n'
    keys = dictionary.keys()
    for key in keys:
        value = dictionary.get(key)
        res += f'{indent}{INDENTS["big"]}{key}:{INDENTS["low"]}'
        res += get_values(value, depth)
    res += indent + '}\n'
    return res


def stylish_format(diff):
    depth = 0
    result = '{\n'
    keys = diff.keys()
    for key in keys:
        child = diff[key]
        result += converter(key, child, depth)
    result += '}'
    return result


def converter(key, child, depth):
    indent = INDENTS["big"] * depth
    status, value = child['status'], child['value']
    results = ''
    if status == 'nested':
        results += f'{indent}{INDENTS["big"]}{key}:{INDENTS["low"]}'
        results += '{\n'
        for k, v in value.items():
            results += converter(k, v, depth + 1)
        results += f'{indent}{INDENTS["big"]}'
        results += '}\n'
    elif status == 'changed':
        value1, value2 = value
        results += f'{indent}{INDENTS["-"]}{key}:' \
                   f'{INDENTS["low"]}'
        results += get_values(value1, depth)
        results += f'{indent}{INDENTS["+"]}{key}:' \
                   f'{INDENTS["low"]}'
        results += get_values(value2, depth)
    elif status == 'added':
        results = f'{indent}{INDENTS["+"]}{key}:' \
                  f'{INDENTS["low"]}'
        results += get_values(value, depth)
    elif status == 'deleted':
        results = f'{indent}{INDENTS["-"]}{key}:' \
                  f'{INDENTS["low"]}'
        results += get_values(value, depth)
    elif status == 'unchanged':
        results = f'{indent}{INDENTS["big"]}{key}:' \
                  f'{INDENTS["low"]}'
        results += get_values(value, depth)
    return results


def get_values(value, depth):
    if isinstance(value, dict):
        return convert(value, depth + 1)
    else:
        if not isinstance(value, str):
            return f'{json.dumps(value)}\n'
        else:
            return f'{value}\n'
