from gendiff.diff import generate_diff

correct_answer = """
{
  "- follow": false,
  " host": "hexlet.io",
  "- proxy": "123.234.53.22",
  "+ timeout": 50,
  "- timeout": 20,
  "+ verbose": true
}
"""


def test_generate_diff():
    first_file_path = 'gendiff/tests/fixture/files/file1.`json'
    second_file_path = 'gendiff/tests/fixture/files/file2.json'
    result = generate_diff(first_file_path, second_file_path)
    assert result == correct_answer
