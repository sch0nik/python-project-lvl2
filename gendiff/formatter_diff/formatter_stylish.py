"""Модуль для форматтера stylish."""
from gendiff import processing_diff as diff

BASE_TAB = 4


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
        keys.sort()
        result = ''
        indent = f'{space * (tab  + BASE_TAB)}'
        for item in keys:  # noqa: WPS519
            result += (
                indent + f'{item}: {shaping(value[item], tab + BASE_TAB)}\n'
            )
        return f'{{\n{result}{space * tab}}}'
    return str(value)


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

    # Строковые константы для вывода.
    dict_diff = {
        diff.STATE_ADD: '+ {0}: {1}\n',
        diff.STATE_UPDATE: '- {0}: {2}\n{3}+ {0}: {1}\n',
        diff.STATE_REMOVE: '- {0}: {1}\n',
        diff.STATE_UNMODIFIED: '  {0}: {1}\n',
        diff.STATE_NESTED: '{0}: {1}\n',
    }

    space = f'{space: >{tab}}'
    for item in data:
        name = diff.get_name(item)
        current_state = diff.get_state(item)

        if diff.is_node(item):
            tmp = f'{format_stylish(diff.get_children(item), BASE_TAB + tab)}'
            tmp = dict_diff[current_state].format(name, tmp, '', space)
            tmp = space + tmp
        else:
            value = shaping(diff.get_value(item), tab)
            old_value = shaping(diff.get_old_value(item), tab)
            tmp = space[:-2] + dict_diff[current_state].format(
                name,
                value,
                old_value,
                space[:-2],
            )

        result += tmp

    return f'{{\n{result}{space[:-4]}}}'
