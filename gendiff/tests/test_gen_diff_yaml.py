from gendiff.diff import generate_diff
import pytest
import os


@pytest.mark.parametrize(
    'first_file, second_file, result_file',
    [
        ('gendiff/tests/fixtures/yaml/file1.yaml',
         'gendiff/tests/fixtures/yaml/file2.yaml',
         'gendiff/tests/fixtures/yaml/correct_answer_yaml')
    ],
)
def test_generate_diff(first_file, second_file, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file) == result
