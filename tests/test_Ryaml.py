from gendiff.gendiff import generate_diff
import pytest
import os


@pytest.mark.parametrize(
    'first_file, second_file, result_file',
    [
        ('tests/fixtures/yaml/Rfile1.yaml',
         'tests/fixtures/yaml/Rfile2.yaml',
         'tests/fixtures/correct_answers/nested')
    ],
)
def test_generate_diff(first_file, second_file, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file) == result