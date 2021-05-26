"""Модуль для фораттера json."""
import json

from gendiff import processing_diff as diff

# Представление в json
# {
#     "ADD": {
#       key: value,
#       key: value,
#       key: {},
#       ....
#     },
#     "REMOVE": {
#         key: value,
#         ...,
#     },
#     "UPDATE": {
#         "ADD": {
#           key: value,
#           key: value,
#           key: {},
#           ....
#         },
#         "REMOVE": {
#             key: value,
#             ...,
#         },
#         ...
#     },
# }


def reformat_diff(data):
    """Реформат data в вид подходящий для json.

    Args:
        data: входдные данные,

    Returns:
        Переделанная data.
    """
    result = {}
    for item in data:
        name = diff.get_str_state(item)
        key = diff.get_name(item)
        if diff.is_value(item):
            value = diff.get_value(item)
        else:
            value = reformat_diff(diff.get_children(item))

        tmp = {key: value}
        if result.get(name):
            result[name].update(tmp)
        else:
            result[name] = tmp
    return result


def format_json(data):
    """Форматирование data в стиле формата json.

    Args:
        data: данные diff,

    Returns:
        Строка diff отформатированная в виде json.
    """
    json_diff = reformat_diff(data)
    return json.dumps(json_diff, indent=2)
