"""Апи для работы с дифом."""
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
    """Проверка что item это элемент с ребенком.

    Т.е. у текущего элемента есть вложенные элементы.
    """
    return item[STATE] == STATE_NESTED


def is_complex(item):
    """Проверка что item это сложное значение.

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
