# Внутренее представление diff:
# diff = [
# {
#     state: ['+', '-', ' '] - состояние, удалили, добавили и т.д.
#     key: key               - ключ из оригинального словаря
#     children: [{}, None]   - либо вложенный словарь, либо None
#     Value: [value, None]   - если children словарь, то None
#                              иначе value
# }, ....
# ]
# from copy import deepcopy


def create_diff():
    return []


def add_delete(key, data, diff):
    diff.append(
        {
            'state': '-',
            'key': key,
            'children': data if type(data) == dict else None,
            'value': None if type(data) == dict else data,
        }
    )


def add_unmodified(key, data, diff):
    diff.append(
        {
            'state': ' ',
            'key': key,
            'children': data if type(data) == dict else None,
            'value': None if type(data) == dict else data,
        }
    )


def add_add(key, data, diff):
    diff.append(
        {
            'state': '+',
            'key': key,
            'children': data if type(data) == dict else None,
            'value': None if type(data) == dict else data,
        }
    )


def add_diff(key, diff1, diff2):
    diff1.extend([
        {
            'state': ' ',
            'key': key,
            'children': diff2,
            'value': None,
        }
    ])


def low_key_word(value):
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def stylish(data, tab=4):
    space = ' '
    result = ''
    if type(data) == dict:
        keys = sorted(list(data.keys()))
        for item_dict in keys:
            tmp = f'{tab * space}{item_dict}: '
            if type(data[item_dict]) != dict:
                result += (
                    f'{tmp}'
                    f'{low_key_word(data[item_dict])}\n'
                )
            else:
                result += (
                    f'{tmp}'
                    f'{low_key_word(stylish(data[item_dict], tab + 4))}\n'
                )
    else:
        new_data = sorted(data, key=lambda x: x['key'])
        for item in new_data:
            tmp = f'{item["state"].rjust(tab - 1, space)} {item["key"]}: '
            if item['children'] is None:
                result += f'{tmp}{low_key_word(item["value"])}\n'
            else:
                result += f"{tmp}{stylish(item['children'], tab + 4)}\n"
    result = f'{{\n{result}{(tab - 4) * space}}}'
    return result
