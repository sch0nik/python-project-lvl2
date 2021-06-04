"""Модуль для форматтера stylish."""
from gendiff.processing_diff import apy_diff as diff

BASE_TAB = 4


def value_formatting(value, tab):
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
        result = ''
        indent = f'{space * (tab  + BASE_TAB)}'
        for item in keys:  # noqa: WPS519
            result += indent
            result += (
                f'{item}: '
                f'{value_formatting(value[item], tab + BASE_TAB)}\n'
            )
        return f'{{\n{result}{space * tab}}}'
    return str(value)


def format_stylish(data, tab=BASE_TAB):  # noqa: WPS210  # noqa: WPS210
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
    indent = space[:-2]
    for item in data:
        name = diff.get_name(item)
        current_state = diff.get_state(item)

        if diff.is_node(item):
            node = diff.get_children(item)
            formatted_node = f'{format_stylish(node, BASE_TAB + tab)}'
            tmp = space + dict_diff[current_state].format(
                name,
                formatted_node,
                '',
                space,
            )
        else:
            value = value_formatting(diff.get_value(item), tab)
            old_value = value_formatting(diff.get_old_value(item), tab)
            tmp = indent + dict_diff[current_state].format(
                name,
                value,
                old_value,
                indent,
            )

        result += tmp

    return f'{{\n{result}{space[:-4]}}}'
