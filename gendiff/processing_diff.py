# Внутренее представление diff:
# diff = [
# {
#     state: ['+', '-', ' ', '_' ] - состояние:
#                                       +   добавили,
#                                       -   удалили,
#                                       _   именилось значение
#                                       ' ' неизменился,
#     key: key               - ключ из оригинального словаря
#     children: {}, None     - либо список словарей, либо None
#     value: value, None     - если children список, то None
#                              иначе value
#     old_value: value        - только для случаев когда ключ остался,
#                              а значение изменилось
# }, ....
# ]
import copy
STATE_ADD = '+'
STATE_REMOVE = '-'
STATE_UNMODIFIED = ' '
STATE_UPDATE = '_'


def create_diff():
    return []


def add_delete(key, data, diff):
    new_data = copy.deepcopy(data)
    diff.append(
        {
            'state': STATE_REMOVE,
            'key': key,
            'children': None,
            'value': new_data,
        }
    )


def add_unmodified(key, data, diff):
    new_data = copy.deepcopy(data)
    diff.append(
        {
            'state': STATE_UNMODIFIED,
            'key': key,
            'children': None,
            'value': new_data,
        }
    )


def add_update(key, data1, data2, diff):
    new_data1 = copy.deepcopy(data1)
    new_data2 = copy.deepcopy(data2)
    diff.append(
        {
            'state': STATE_UPDATE,
            'key': key,
            'old_value': new_data1,
            'children': None,
            'value': new_data2,
        }
    )


def add_add(key, data, diff):
    new_data = copy.deepcopy(data)
    diff.append(
        {
            'state': STATE_ADD,
            'key': key,
            'children': None,
            'value': new_data,
        }
    )


def add_diff(key, diff1, diff2):
    diff1.extend([
        {
            'state': STATE_UNMODIFIED,
            'key': key,
            'children': diff2,
            'value': None,
        }
    ])


def get_name(data):
    return data['key']


def get_state(data):
    return data['state']


def get_value(data):
    return data['value']


def get_children(data):
    return data['children']


def is_value(data):
    if type(data) == list:
        return False
    return data.get('children') is None


def is_node(data):
    return not data.get('children') is None


def is_complex(data):
    return type(data) == dict


def get_old_value(data):
    return data.get('old_value')


def sort_alphabetically(data):
    return sorted(data, key=lambda x: x['key'])
