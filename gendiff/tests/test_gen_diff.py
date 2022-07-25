from gendiff.diff import generate_diff
import pytest
import os


@pytest.mark.parametrize(
    'first_file, second_file, result_file',
    [
        ('gendiff/tests/fixtures/file1.json',
         'gendiff/tests/fixtures/file2.json',
         'gendiff/tests/fixtures/correct_answer')
    ],
)
def test_generate_diff(first_file, second_file, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file) == result
    assert type(result) == str
    assert type(generate_diff(first_file, second_file)) == str
