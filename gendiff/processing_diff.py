"""Модуль внутреннего представления дифа."""
# Внутренее представление diff:
# Это список словарей diff = [
# { state: ['added', 'removed', ... ] - состояние:
#                                'added'     добавили,
#                                'removed'   удалили,
#                                'updated'   именилось значение
#                                'unmodfied' неизменился,
#                                'nested'    вложенный,
#     key: key                  - ключ из оригинального словаря
#     children: [{}, {}], None  - либо список словарей, либо None
#     value: value, None        - если children список, то None
#                                 иначе value
#     old_value: value          - только для случаев когда ключ остался,
#                                 а значение изменилось
# }, ....]
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
    # diff.sort(key=lambda item: item[KEY])


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
    # diff.sort(key=lambda item: item[KEY])


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
    # diff.sort(key=lambda item: item[KEY])


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
    # diff.sort(key=lambda item: item[KEY])


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
    # diff1.sort(key=lambda item: item[KEY])


def get_name(item):
    """Возвращает имя элемента."""
    return item[KEY]


def get_state(item):
    """Возвращает состояние элемента."""
    return item[STATE]


def get_value(item):
    """Возвращает значение элемента."""
    return item[VALUE]


def get_children(item):
    """Возвращает детей элемента."""
    return item[CHILDREN]


def is_node(item):
    """Проверка что data это элемент с ребенком.

    Т.е. у текущего элемента есть вложенные элементы.
    """
    return item[STATE] == STATE_NESTED


def is_complex(item):
    """Проверка что data это сложное значение.

    Для форматтера plain.
    """
    return isinstance(item, dict)


def get_old_value(item):
    """Возврат старого значение.

    Для ключей у которых изменились значения.
    """
    return item.get(OLD_VALUE)


def get_str_state(item):
    """Вывод состояния элемента в строку."""
    state = item[STATE]
    if state == STATE_ADD:
        return 'ADD'
    if state == STATE_REMOVE:
        return 'REMOVE'
    if state == STATE_UNMODIFIED:
        return 'UNMODIFIED'
    if state == STATE_UPDATE:
        return 'UPDATE'
    if state == STATE_NESTED:
        return 'UPDATE'
