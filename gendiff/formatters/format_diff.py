"""Выбор формата вывода дифа."""
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def format(diff, formatter):
    """Выбор формата вывода дифа."""
    if formatter == 'stylish':
        return format_stylish(diff)
    elif formatter == 'plain':
        return format_plain(diff)
    elif formatter == 'json':
        return format_json(diff)
    return 'Не известный формат.'
