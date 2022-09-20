from gendiff.gendiff import generate_diff
import pytest
import os

JSON_1 = 'tests/fixtures/json/file1.json'
JSON_2 = 'tests/fixtures/json/file2.json'
RJSON_1 = 'tests/fixtures/json/Rfile1.json'
RJSON_2 = 'tests/fixtures/json/Rfile2.json'
YAML_1 = 'tests/fixtures/yaml/file1.yaml'
YAML_2 = 'tests/fixtures/yaml/file2.yaml'
YML_1 = 'tests/fixtures/yaml/file1.yml'
YML_2 = 'tests/fixtures/yaml/file2.yml'
RYAML_1 = 'tests/fixtures/yaml/Rfile1.yaml'
RYAML_2 = 'tests/fixtures/yaml/Rfile2.yaml'
RYML_1 = 'tests/fixtures/yaml/Rfile1.yml'
RYML_2 = 'tests/fixtures/yaml/Rfile2.yml'

CORRECT_JSON = 'tests/fixtures/correct_answers/json'
CORRECT_FLAT = 'tests/fixtures/correct_answers/flat'
CORRECT_NESTED = 'tests/fixtures/correct_answers/nested'
CORRECT_PLAIN = 'tests/fixtures/correct_answers/plain'


@pytest.mark.parametrize(
    'first_file, second_file, format_, result_file',
    [
        (JSON_1, JSON_2, 'stylish', CORRECT_FLAT),
        (RJSON_1, RJSON_2, 'stylish', CORRECT_NESTED),
        (YML_1, YML_2, 'stylish', CORRECT_FLAT),
        (YAML_1, YAML_2, 'stylish', CORRECT_FLAT),
        (RYAML_1, RYAML_2, 'stylish', CORRECT_NESTED),
        (RYML_1, RYML_2, 'stylish', CORRECT_NESTED),
        (RJSON_1, RJSON_2, 'plain', CORRECT_PLAIN),
        (RJSON_1, RJSON_2, 'json', CORRECT_JSON),
    ],
)
def test_generate_diff(first_file, second_file, format_, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file, format_) == result
