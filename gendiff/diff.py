import json


def open_files(first_file, second_file):
    with open(first_file) as f1:
        file1 = json.load(f1)
    with open(second_file) as f2:
        file2 = json.load(f2)
    return file1, file2


def filtered_values(values, dict):
    values_copy = list(values.copy())
    for value in values:
        if value in dict:
            values_copy.remove(value)
            values_copy.insert(0, value)
    return values_copy


def generate_diff(first_path, second_path):
    first_dict, second_dict = open_files(first_path, second_path)
    identical = first_dict.items() & second_dict.items()
    missed = first_dict.items() - second_dict.items()
    extra = second_dict.items() - first_dict.items()
    all_values = identical | missed | extra
    all_values = filtered_values(all_values, first_dict)
    sorted_pairs = sorted(
        all_values, key=lambda pair: pair[0].lower()
    )
    diff = []

    for i, j in sorted_pairs:
        if (i, j) in missed:
            diff.append(("- " + i, j))
        elif (i, j) in extra:
            diff.append(('+ ' + i, j))
        else:
            diff.append((" " + i, j))
    diff = json.dumps(dict(diff), indent=2)
    return diff
