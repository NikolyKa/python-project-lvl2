import json


def stylish(dict_):
    depth = 0
    result = '{\n'
    keys = dict_.keys()
    for key in keys:
        child = dict_[key]

        def converter(key, child, depth):
            indent = "    " * depth
            status, value = child['status'], child['value']
            results = ''
            if status == 'nested':
                results += f'{indent}    {key}:' + ' {\n'
                for k, v in value.items():
                    results += converter(k, v, depth + 1)
                results += indent + "    " + '}\n'
            elif status == 'changed':
                val1 = value[0]
                val2 = value[1]
                results += f'{indent}  - {key}:' + values(val1, depth)
                results += f'{indent}  + {key}:' + values(val2, depth)
            elif status == 'added':
                results = f'{indent}  + {key}:' + values(value, depth)
            elif status == 'deleted':
                results = f'{indent}  - {key}:' + values(value, depth)
            elif status == 'unchanged':
                results = f'{indent}    {key}:' + values(value, depth)
            return results

        result += converter(key, child, depth)
    result += "}"
    return result


def values(value, depth):
    if isinstance(value, dict):
        return convert_dict_to_str(value, depth + 1)
    elif len(str(value)) == 0:
        return '\n'
    else:
        if not isinstance(value, str):
            return f' {json.dumps(value)}\n'
        else:
            return f' {value}\n'


def convert_dict_to_str(dictionary, depth):
    indent = "    " * depth
    result = ' {\n'
    keys = dictionary.keys()
    for key in keys:
        value = dictionary.get(key)
        result += f'{indent}    {key}:' + values(value, depth)
    result += indent + '}\n'
    return result
