import json


def plain(data, path=[]):
    result = []
    keys = data.keys()
    for key in keys:
        child = data.get(key)
        status, value = child['status'], child['value']
        path.append(key)
        if status == 'deleted':
            result.append(f"Property '{'.'.join(path)}' was removed")
        elif status == 'added':
            value = convert(value)
            result.append(f"Property '{'.'.join(path)}' "
                          f"was added with value: {value}")
        elif status == 'changed':
            values = []
            for i in value:
                values.append(convert(i))
            result.append(f"Property '{'.'.join(path)}' was updated. "
                          f"From {values[0]} to {values[1]}")
        elif status == 'nested':
            result.append(plain(value))
        path.pop()
    return '\n'.join(result)


def convert(data):
    if isinstance(data, dict):
        return "[complex value]"
    elif isinstance(data, str):
        return f"'{data}'"
    if not isinstance(data, str):
        return json.dumps(data)
    else:
        return data
