def collect_diff_segments(first_dict, second_dict):
    keys = first_dict.keys() | second_dict.keys()
    sorted_keys = sorted(keys)
    result = {}
    for key in sorted_keys:
        value1, value2 = first_dict.get(key), second_dict.get(key)

        if key not in first_dict:
            status = 'added'
            value = value2

        elif key not in second_dict:
            status = 'deleted'
            value = value1

        elif value1 == value2:
            status = 'unchanged'
            value = value1

        elif isinstance(value1, dict) and isinstance(value2, dict):
            status = 'nested'
            value = collect_diff_segments(value1, value2)

        elif value1 != value2:
            status = 'changed'
            value = value1, value2

        result[key] = {
            'status': status,
            'value': value}

    return result
