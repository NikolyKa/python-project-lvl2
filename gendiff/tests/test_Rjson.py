from gendiff.diff import generate_diff
import pytest
import os


@pytest.mark.parametrize(
    'first_file, second_file, result_file',
    [
        ('Rfile1.json',
         'Rfile2.json',
         'gendiff/tests/fixtures/correct_answers/nested')
    ],
)
def test_generate_diff(first_file, second_file, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file) == result
