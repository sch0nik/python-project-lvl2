from gendiff.generate_difference import generate_diff


def test_generate_diff_json_recurs():
    result_file = open('tests/fixtures/result_recurs')
    expected_result = result_file.read()
    expected_result = expected_result[:-1]
    result_file.close()
    file_a = 'tests/fixtures/file1_recurs.json'
    file_b = 'tests/fixtures/file2_recurs.json'
    received_result = generate_diff(file_a, file_b, 'stylish')

    assert received_result == expected_result


def test_generate_diff_yaml_recurs():
    result_file = open('tests/fixtures/result_recurs')
    expected_result = result_file.read()
    expected_result = expected_result[:-1]
    result_file.close()
    file_a = 'tests/fixtures/file1_recurs.yaml'
    file_b = 'tests/fixtures/file2_recurs.yaml'
    received_result = generate_diff(file_a, file_b, 'stylish')

    assert received_result == expected_result
