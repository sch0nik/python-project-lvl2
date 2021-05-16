from gendiff.generate_difference import generate_diff


def test_generate_diff_plain():
    result_file = open('tests/fixtures/result_plain')
    expected_result_plain = result_file.read()
    result_file.close()

    result_file = open('tests/fixtures/result_stylish')
    expected_result_stylish = result_file.read()
    expected_result_stylish = expected_result_stylish[:-1]
    result_file.close()

    json_file_a = 'tests/fixtures/file1.json'
    json_file_b = 'tests/fixtures/file2.json'
    received_result_stylish_json = generate_diff(json_file_a, json_file_b, 'stylish')
    received_result_plain_json = generate_diff(json_file_a, json_file_b, 'plain')

    yaml_file_a = 'tests/fixtures/file1.yaml'
    yaml_file_b = 'tests/fixtures/file2.yaml'
    received_result_stylish_yaml = generate_diff(yaml_file_a, yaml_file_b, 'stylish')
    received_result_plain_yaml = generate_diff(yaml_file_a, yaml_file_b, 'plain')

    assert received_result_stylish_json == expected_result_stylish
    assert received_result_stylish_yaml == expected_result_stylish
    assert received_result_plain_json == expected_result_plain
    assert received_result_plain_yaml == expected_result_plain
