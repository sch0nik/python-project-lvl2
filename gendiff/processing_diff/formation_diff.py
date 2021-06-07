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


def compare_data(data1, data2):  # noqa: WPS210, WPS231
    """Сравнение двух данных и формирование дифа."""
    diff = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        type_data = (
            isinstance(value1, dict) and isinstance(value2, dict)
        )
        if key in data1 and key not in data2:
            diff.append(
                {
                    STATE: STATE_REMOVE,
                    KEY: key,
                    CHILDREN: None,
                    VALUE: deepcopy(value1),
                },
            )
        elif key not in data1 and key in data2:
            diff.append(
                {
                    STATE: STATE_ADD,
                    KEY: key,
                    CHILDREN: None,
                    VALUE: deepcopy(value2),
                },
            )
        elif value1 == data2[key]:
            diff.append(
                {
                    STATE: STATE_UNMODIFIED,
                    KEY: key,
                    CHILDREN: None,
                    VALUE: deepcopy(value2),
                },
            )

        elif type_data:
            diff.extend([
                {
                    STATE: STATE_NESTED,
                    KEY: key,
                    CHILDREN: compare_data(value1, value2),
                    VALUE: None,
                },
            ])
        else:
            diff.append(
                {
                    STATE: STATE_UPDATE,
                    KEY: key,
                    OLD_VALUE: deepcopy(value1),
                    CHILDREN: None,
                    VALUE: deepcopy(value2),
                },
            )

    return diff
