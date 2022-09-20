import json

INDENTS = {'big': "    ", 'low': " ", '-': '  - ', '+': '  + '}


def convert(dictionary, depth):
    indent = INDENTS["big"] * depth
    res = '{\n'
    keys = dictionary.keys()
    for key in keys:
        value = dictionary.get(key)
        res += f'{indent}{INDENTS["big"]}{key}:{INDENTS["low"]}'\
               + values(value, depth)
    res += indent + '}\n'
    return res


def stylish_format(diff):
    depth = 0
    result = '{\n'
    keys = diff.keys()
    for key in keys:
        child = diff[key]

        def converter(key, child, depth):
            indent = INDENTS["big"] * depth
            status, value = child['status'], child['value']
            results = ''
            if status == 'nested':
                results += f'{indent}{INDENTS["big"]}{key}:{INDENTS["low"]}'\
                           + '{\n'
                for k, v in value.items():
                    results += converter(k, v, depth + 1)
                results += indent + INDENTS["big"] + '}\n'
            elif status == 'changed':
                val1 = value[0]
                val2 = value[1]
                results += f'{indent}{INDENTS["-"]}{key}:' \
                           f'{INDENTS["low"]}' + values(val1, depth)
                results += f'{indent}{INDENTS["+"]}{key}:' \
                           f'{INDENTS["low"]}' + values(val2, depth)
            elif status == 'added':
                results = f'{indent}{INDENTS["+"]}{key}:' \
                          f'{INDENTS["low"]}' + values(value, depth)
            elif status == 'deleted':
                results = f'{indent}{INDENTS["-"]}{key}:' \
                          f'{INDENTS["low"]}' + values(value, depth)
            elif status == 'unchanged':
                results = f'{indent}{INDENTS["big"]}{key}:' \
                          f'{INDENTS["low"]}' + values(value, depth)
            return results

        result += converter(key, child, depth)
    result += "}"
    return result


def values(value, depth):
    if isinstance(value, dict):
        return convert(value, depth + 1)
    else:
        if not isinstance(value, str):
            return f'{json.dumps(value)}\n'
        else:
            return f'{value}\n'
