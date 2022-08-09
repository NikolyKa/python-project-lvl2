import json


def convert(dictionary, depth):
    indent = "    " * depth
    res = '{\n'
    keys = dictionary.keys()
    for key in keys:
        value = dictionary.get(key)
        res += f'{indent}    {key}: ' + values(value, depth)
    res += indent + '}\n'
    return res


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
                results += f'{indent}    {key}: ' + '{\n'
                for k, v in value.items():
                    results += converter(k, v, depth + 1)
                results += indent + "    " + '}\n'
            elif status == 'changed':
                val1 = value[0]
                val2 = value[1]
                results += f'{indent}  - {key}: ' + values(val1, depth)
                results += f'{indent}  + {key}: ' + values(val2, depth)
            elif status == 'added':
                results = f'{indent}  + {key}: ' + values(value, depth)
            elif status == 'deleted':
                results = f'{indent}  - {key}: ' + values(value, depth)
            elif status == 'unchanged':
                results = f'{indent}    {key}: ' + values(value, depth)
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
