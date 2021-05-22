"""Модуль для форматтера plain."""
from gendiff import processing_diff as diff

PROPERTY_ADDED = "Property \'{}\' was added with value: {}"
PROPERTY_UPDATED = "Property \'{}\' was updated. From {} to {}"
PROPERTY_REMOVED = "Property \'{}\' was removed"
COMPLEX_VALUE = '[complex value]'
SEPARATOR = '.'


def shaping(value):
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
    elif diff.is_complex(value):
        return COMPLEX_VALUE
    return f"\'{str(value)}\'"


def format_plain(data, parents):
    """Форматтер plain.

    Args:
        data: сам diff.
        parents: список имен вложенности.

    Returns:
        format_str: строка приведенная к нужному виду.
    """
    format_str = ''
    data = diff.sort_alphabetically(data)

    for item in data:
        name = parents + [diff.get_name(item)]
        if diff.is_node(item):
            format_str += format_plain(diff.get_children(item), name)
        else:
            current_state = diff.get_state(item)
            name = SEPARATOR.join(name)
            value = shaping(diff.get_value(item))
            old_value = shaping(diff.get_old_value(item))

            if current_state == diff.STATE_ADD:
                format_str += PROPERTY_ADDED.format(name, value) + '\n'

            elif current_state == diff.STATE_UPDATE:
                format_str += (
                    PROPERTY_UPDATED.format(name, old_value, value) + '\n'
                )

            elif current_state == diff.STATE_REMOVE:
                format_str += PROPERTY_REMOVED.format(name) + '\n'

    return format_str
