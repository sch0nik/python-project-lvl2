from gendiff.generate_difference import generate_diff


def test_generate_diff_plain():
    result_file = open('tests/fixtures/result_plain')
    expected_result = result_file.read()
    result_file.close()

    file_a = 'tests/fixtures/file1.json'
    file_b = 'tests/fixtures/file2.json'
    received_result_json = generate_diff(file_a, file_b, 'plain')

    file_a = 'tests/fixtures/file1.yaml'
    file_b = 'tests/fixtures/file2.yaml'
    received_result_yaml = generate_diff(file_a, file_b, 'plain')

    assert received_result_json == expected_result
    assert received_result_yaml == expected_result


def test_generate_diff_stylish():
    result_file = open('tests/fixtures/result_stylish')
    expected_result_stylish = result_file.read()
    expected_result_stylish = expected_result_stylish[:-1]
    result_file.close()

    file_a = 'tests/fixtures/file1.json'
    file_b = 'tests/fixtures/file2.json'
    received_result_json = generate_diff(file_a, file_b, 'stylish')

    file_a = 'tests/fixtures/file1.yaml'
    file_b = 'tests/fixtures/file2.yaml'
    received_result_yaml = generate_diff(file_a, file_b, 'stylish')

    assert received_result_json == expected_result_stylish
    assert received_result_yaml == expected_result_stylish
