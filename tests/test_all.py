import json
import yaml

from gendiff.generate_difference import compare_dict


def test_generate_diff():
    result_file = open('tests/fixtures/result')
    expected_result = ''
    for line in result_file:
        expected_result += line

    file_a = json.load(open('tests/fixtures/fileA.json'))
    file_b = json.load(open('tests/fixtures/fileB.json'))
    received_result = compare_dict(file_a, file_b)
    assert received_result == expected_result


def test_gendiff_yaml():
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    file_a = yaml.full_load(open('tests/fixtures/fileA.yaml'))
    file_b = yaml.full_load(open('tests/fixtures/fileB.yaml'))
    received_result = compare_dict(file_a, file_b)
    assert received_result == expected_result
