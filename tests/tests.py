from gendiff.gendiff import generate_diff
import pytest
import os

json_1 = 'tests/fixtures/json/file1.json'
json_2 = 'tests/fixtures/json/file2.json'
Rjson_1 = 'tests/fixtures/json/Rfile1.json'
Rjson_2 = 'tests/fixtures/json/Rfile2.json'
yaml_1 = 'tests/fixtures/yaml/file1.yaml'
yaml_2 = 'tests/fixtures/yaml/file2.yaml'
yml_1 = 'tests/fixtures/yaml/file1.yml'
yml_2 = 'tests/fixtures/yaml/file2.yml'
Ryaml_1 = 'tests/fixtures/yaml/Rfile1.yaml'
Ryaml_2 = 'tests/fixtures/yaml/Rfile2.yaml'
Ryml_1 = 'tests/fixtures/yaml/Rfile1.yml'
Ryml_2 = 'tests/fixtures/yaml/Rfile2.yml'

correct_json = 'tests/fixtures/correct_answers/json'
correct_flat = 'tests/fixtures/correct_answers/flat'
correct_nested = 'tests/fixtures/correct_answers/nested'
correct_plain = 'tests/fixtures/correct_answers/plain'


@pytest.mark.parametrize(
    'first_file, second_file, format_, result_file',
    [
        (json_1, json_2, 'stylish', correct_flat),
        (Rjson_1, Rjson_2, 'stylish', correct_nested),
        (yml_1, yml_2, 'stylish', correct_flat),
        (yaml_1, yaml_2, 'stylish', correct_flat),
        (Ryaml_1, Ryaml_2, 'nested', correct_nested),
        (Ryml_1, Ryml_2, 'nested', correct_nested),
        (Rjson_1, Rjson_2, 'plain', correct_plain),
        (Rjson_1, Rjson_2, 'json', correct_json),
    ],
)
def test_generate_diff(first_file, second_file, format_, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file, format_) == result
