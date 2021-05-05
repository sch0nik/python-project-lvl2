import json

from gendiff.difference import generate_diff


def test_generate_diff():
    result_file = open('tests/fixtures/result')
    expected_result = ''
    for line in result_file:
        expected_result += line

    file_a = json.load(open('tests/fixtures/fileA.json'))
    file_b = json.load(open('tests/fixtures/fileB.json'))
    received_result = generate_diff(file_a, file_b)
    assert received_result == expected_result
