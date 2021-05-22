import json
# import copy


def format_json(data):
    # new_data = {}
    # for item in data:

    f = open('tests/fixtures/result_json.json', 'w')
    json.dump(data, f, indent=2)
    f.close()

    return data
