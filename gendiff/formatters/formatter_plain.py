"""Модуль для форматтера plain."""
from gendiff.processing_diff import apy_diff as diff


def value_formatting(value):
    """Приведение value к нужной форме.

    Args:
        value: значение, которое нужно привести к заданной форме.

    Returns:
        Форматированная строка.
    """
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    elif diff.is_complex(value):
        return '[complex value]'
    return f"\'{str(value)}\'"


def format_plain(data, parents=''):  # noqa: WPS210
    """Форматирование вывода в виде plain."""
    # Словарь строковых констант.
    dict_diff = {
        diff.STATE_ADD: "Property \'{0}\' was added with value: {1}",
        diff.STATE_UPDATE: "Property \'{0}\' was updated. From {2} to {1}",
        diff.STATE_REMOVE: "Property \'{0}\' was removed",
        diff.STATE_UNMODIFIED: '',
    }

    format_str = []
    for item in data:

        name = diff.get_name(item)
        name = f'{parents}.{name}' if parents else name
        current_state = diff.get_state(item)

        if diff.is_node(item):
            tmp = format_plain(diff.get_children(item), name)
        else:
            value = value_formatting(diff.get_value(item))
            old_value = value_formatting(diff.get_old_value(item))
            tmp = dict_diff[current_state].format(name, value, old_value)

        format_str.append(tmp)

    format_str = [item for item in format_str if item]
    format_str = '\n'.join(format_str)
    return format_str
