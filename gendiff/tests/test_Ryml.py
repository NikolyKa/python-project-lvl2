from gendiff.diff import generate_diff
import pytest
import os


@pytest.mark.parametrize(
    'first_file, second_file, result_file',
    [
        ('gendiff/tests/fixtures/yaml/Rfile1.yml',
         'gendiff/tests/fixtures/yaml/Rfile2.yml',
         'gendiff/tests/fixtures/correct_answers/nested')
    ],
)
def test_generate_diff(first_file, second_file, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file) == result
