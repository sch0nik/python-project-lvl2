from os.path import join
from gendiff.generate_difference import generate_diff


def paths(case):
    dict_case = {
        'tests': 'tests',
        'fixtures': 'fixtures',

        'file1.json': 'file1.json',
        'file2.json': 'file2.json',

        'file1.yaml': 'file1.yaml',
        'file2.yaml': 'file2.yaml',

        'result_plain': 'result_plain',
        'result_stylish': 'result_stylish',
        'result_json.json': 'result_json.json',
    }
    return join(
        dict_case['tests'],
        dict_case['fixtures'],
        dict_case[case],
    )


def test_generate_diff_plain():
    result_file = open(paths('result_plain'))
    expected_result = result_file.read()
    expected_result.strip()
    result_file.close()

    file_a = paths('file1.json')
    file_b = paths('file2.json')
    received_result_json = generate_diff(file_a, file_b, 'plain')

    file_a = paths('file1.yaml')
    file_b = paths('file2.yaml')
    received_result_yaml = generate_diff(file_a, file_b, 'plain')

    assert received_result_yaml == expected_result
    assert received_result_json == expected_result


def test_generate_diff_stylish():
    result_file = open(paths('result_stylish'))
    expected_result = result_file.read()
    expected_result.strip()
    result_file.close()

    file_a = paths('file1.json')
    file_b = paths('file2.json')
    received_result_json = generate_diff(file_a, file_b, 'stylish')

    file_a = paths('file1.yaml')
    file_b = paths('file2.yaml')
    received_result_yaml = generate_diff(file_a, file_b, 'stylish')

    assert received_result_json == expected_result
    assert received_result_yaml == expected_result


def test_generate_diff_json():
    result_file = open(paths('result_json.json'))
    expected_result = result_file.read()
    expected_result.strip()
    result_file.close()

    file_a = paths('file1.json')
    file_b = paths('file2.json')
    received_result_json = generate_diff(file_a, file_b, 'json')

    assert received_result_json == expected_result
