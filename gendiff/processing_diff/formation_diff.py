"""Формирование дифа.

Внутренее представление diff:
Это список словарей diff = [
{ state: ['added', 'removed', ... ] - состояние:
                               'added'     - добавили,
                               'removed'   - удалили,
                               'updated'   - именилось значение
                               'unmodfied' - неизменился,
                               'nested'    - вложенный,
  key: key                  - ключ из оригинального словаря
  children: [{}, {}], None  - либо список словарей, либо None
  value: value, None        - если children список, то None
                              иначе value
  old_value: value          - только для случаев когда ключ остался,
                              а значение изменилось
}, ....]
"""
from copy import deepcopy


STATE_ADD = 'added'
STATE_REMOVE = 'removed'
STATE_UNMODIFIED = 'unmodfied'
STATE_UPDATE = 'updated'
STATE_NESTED = 'nested'

STATE = 'state'
KEY = 'key'
CHILDREN = 'children'
VALUE = 'value'
OLD_VALUE = 'old_value'


def create_diff():
    """Дифф это список."""
    return []


def add_delete(key, data, diff):
    """Добавление удаленного элемента."""
    new_data = deepcopy(data)
    diff.append(
        {
            STATE: STATE_REMOVE,
            KEY: key,
            CHILDREN: None,
            VALUE: new_data,
        },
    )


def add_unmodified(key, data, diff):
    """Добавление неизмененного элемента."""
    new_data = deepcopy(data)
    diff.append(
        {
            STATE: STATE_UNMODIFIED,
            KEY: key,
            CHILDREN: None,
            VALUE: new_data,
        },
    )


def add_update(key, data1, data2, diff):
    """Добавление измененного элемента."""
    new_data1 = deepcopy(data1)
    new_data2 = deepcopy(data2)
    diff.append(
        {
            STATE: STATE_UPDATE,
            KEY: key,
            OLD_VALUE: new_data1,
            CHILDREN: None,
            VALUE: new_data2,
        },
    )


def add_add(key, data, diff):
    """Добавление добавленного элемента."""
    new_data = deepcopy(data)
    diff.append(
        {
            STATE: STATE_ADD,
            KEY: key,
            CHILDREN: None,
            VALUE: new_data,
        },
    )


def add_diff(key, diff1, diff2):
    """Добавление вложенного дифа."""
    diff1.extend([
        {
            STATE: STATE_NESTED,
            KEY: key,
            CHILDREN: diff2,
            VALUE: None,
        },
    ])


def compare_data(data1, data2):  # noqa: WPS231
    """Сравнение двух данных и формирование дифа."""
    diff = create_diff()
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        type_data = (
            isinstance(data1.get(key), dict) and  # noqa: W504
            isinstance(data2.get(key), dict)
        )
        if key in data1 and key not in data2:
            add_delete(key, data1[key], diff)
        elif key not in data1 and key in data2:
            add_add(key, data2[key], diff)  # noqa: WPS204
        elif data1[key] == data2[key]:
            add_unmodified(key, data2[key], diff)
        elif type_data:
            add_diff(key, diff, compare_data(data1[key], data2[key]))
        else:
            add_update(key, data1[key], data2[key], diff)

    return diff
