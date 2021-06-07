from gendiff.formatters import format_json, format_plain, format_stylish


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
    elif formatter == 'plain':
        return format_plain(diff)
    elif formatter == 'json':
        return format_json(diff)
    return 'Не известный формат.'
