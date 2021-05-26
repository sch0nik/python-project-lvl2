"""Модуль для форматтера stylish."""
from gendiff import processing_diff as diff

BASE_TAB = 4
ELEMENT_ADD = '+ '
ELEMENT_REMOVE = '- '
ELEMENT_UNMODIFIED = ' '


def shaping(value, tab):
    """Приведение value к нужной форме.

    Args:
        value: значение, которое нужно привести к заданной форме.
        tab: количество отступов перед строкой.

    Returns:
        Форматированная строка.
    """
    space = ' '
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        keys = list(value.keys())
        keys = sorted(keys)
        result = ''
        for item in keys:  # noqa: WPS519
            result += (
                f'{space * (tab  + BASE_TAB)}'
                f'{item}: {shaping(value[item], tab + 4)}\n'
            )
        return f'{{\n{result}{space * tab}}}'
    return str(value)


def case(item, tab, name):
    """Составление строки в зависимости от состояния item.

    Args:
        item: проверяемый элемент,
        tab: количество отступов,
        name: значение ключа элемента дифа.

    Returns:
        Строку результата.
    """
    current_state = diff.get_state(item)
    value = shaping(diff.get_value(item), tab)
    old_value = shaping(diff.get_old_value(item), tab)
    tmp = f'{name}: {value}\n'
    tmp_old = f'{name}: {old_value}\n'
    result = ''

    if current_state == diff.STATE_ADD:
        result = f'{ELEMENT_ADD.rjust(tab)}{tmp}'

    elif current_state == diff.STATE_UPDATE:
        result = (
            f'{ELEMENT_REMOVE.rjust(tab)}{tmp_old}'
            f'{ELEMENT_ADD.rjust(tab)}{tmp}'
        )

    elif current_state == diff.STATE_REMOVE:
        result = f'{ELEMENT_REMOVE.rjust(tab)}{tmp}'

    elif current_state == diff.STATE_UNMODIFIED:
        result = f'{ELEMENT_UNMODIFIED.rjust(tab)}{tmp}'

    return result


def format_stylish(data, tab=BASE_TAB):
    """Функция форматирования дифа для вывода в видде stylish.

    Args:
        data: сам диф,
        tab: отступ.

    Returns:
        Форматированная строка в виее styish.
    """
    result = ''
    space = ' '

    for item in data:
        name = diff.get_name(item)
        if diff.is_node(item):
            result += (
                f'{space.rjust(tab)}{name}: '
                f'{format_stylish(diff.get_children(item), BASE_TAB + tab)}\n'
            )
        else:
            result += case(item, tab, name)

    return f'{{\n{result}{space * (tab-4)}}}'
