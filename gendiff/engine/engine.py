def gendiff(first_dict, second_dict):
    keys = first_dict.keys() | second_dict.keys()
    sorted_keys = sorted(keys)
    result = {}
    res = '{\n'
    for key in keys:
        if key not in first_dict:
            result[key] = 'added'
        elif key not in second_dict:
            result[key] = 'deleted'
        elif first_dict[key] == second_dict[key]:
            result[key] = 'unchanged'
        elif first_dict[key] != second_dict[key]:
            result[key] = 'changed'
    for i in sorted_keys:
        if result[i] == 'deleted':
            res += f'  - {i}: {formater(first_dict[i])}\n'
        elif result[i] == 'added':
            res += f'  + {i}: {formater(second_dict[i])}\n'
        elif result[i] == 'unchanged':
            res += f'    {i}: {formater(first_dict[i])}\n'
        elif result[i] == 'changed':
            res += f'  - {i}: {formater(first_dict[i])}\n'
            res += f'  + {i}: {formater(second_dict[i])}\n'
    return res + "}"


def formater(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'none'
    else:
        return str(value)
