from os.path import join
from gendiff.generate_difference import generate_diff

PATH_TESTS = ['tests', 'fixtures']

FILE1_JSON = 'file1.json'
FILE2_JSON = 'file2.json'

FILE1_YAML = 'file1.yaml'
FILE2_YAML = 'file2.yaml'

RESULT_PLAIN = 'result_plain'
RESULT_STYLISH = 'result_stylish'
RESULT_JSON = 'result_json.json'

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def paths(case):
    return join(
        PATH_TESTS[0],
        PATH_TESTS[1],
        case,
    )


def result_file_read(result_file):
    file = open(paths(result_file))
    expected_result = file.read()
    file.close()
    expected_result.strip()
    return expected_result


def received_result(file1, file2, formatt):
    file1 = paths(file1)
    file2 = paths(file2)
    return generate_diff(file1, file2, formatt)


def test_generate_diff_plain():
    expected_result = result_file_read(RESULT_PLAIN)

    received_result_json = received_result(FILE1_JSON, FILE2_JSON, PLAIN)
    received_result_yaml = received_result(FILE1_YAML, FILE2_YAML, PLAIN)

    assert received_result_yaml == expected_result
    assert received_result_json == expected_result


def test_generate_diff_stylish():
    expected_result = result_file_read(RESULT_STYLISH)

    received_result_json = received_result(FILE1_JSON, FILE2_JSON, STYLISH)
    received_result_yaml = received_result(FILE1_YAML, FILE2_YAML, STYLISH)

    assert received_result_json == expected_result
    assert received_result_yaml == expected_result


def test_generate_diff_json():
    expected_result = result_file_read(RESULT_JSON)

    received_result_json = received_result(FILE1_JSON, FILE2_JSON, JSON)
    received_result_yaml = received_result(FILE1_YAML, FILE2_YAML, JSON)

    assert received_result_json == expected_result
    assert received_result_yaml == expected_result
