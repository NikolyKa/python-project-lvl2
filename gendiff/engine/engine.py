def collect_diff_segments(first_dict, second_dict):
    keys = first_dict.keys() | second_dict.keys()
    sorted_keys = sorted(keys)
    result = {}
    for key in sorted_keys:
        val1, val2 = first_dict.get(key), second_dict.get(key)
        if key not in first_dict:
            status = 'added'
            value = val2
        elif key not in second_dict:
            status = 'deleted'
            value = val1
        elif val1 == val2:
            status = 'unchanged'
            value = val1
        elif isinstance(val1, dict) and isinstance(val2, dict):
            status = 'nested'
            value = collect_diff_segments(val1, val2)
        elif val1 != val2:
            status = 'changed'
            value = val1, val2
        result[key] = {
            'status': status,
            'value': value}
    return result
