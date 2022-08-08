from gendiff.gendiff import generate_diff
import pytest
import os


@pytest.mark.parametrize(
    'first_file, second_file, result_file',
    [
        ('gendiff/tests/fixtures/json/file1.json',
         'gendiff/tests/fixtures/json/file2.json',
         'gendiff/tests/fixtures/correct_answers/correct_answer_flat')
    ],
)
def test_generate_diff(first_file, second_file, result_file):
    with open(os.path.abspath(result_file)) as res:
        result = res.read()
    assert generate_diff(first_file, second_file) == result
