"""Формирование дифа."""
from gendiff.processing_diff import processing as proc_diff


def compare_data(data1, data2):  # noqa: WPS231
    """Сравнение двух данных и формирование дифа."""
    diff = proc_diff.create_diff()
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        type_data = (
            isinstance(data1.get(key), dict) and  # noqa: W504
            isinstance(data2.get(key), dict)
        )
        if key in data1 and key not in data2:
            proc_diff.add_delete(key, data1[key], diff)
        elif key not in data1 and key in data2:
            proc_diff.add_add(key, data2[key], diff)  # noqa: WPS204
        elif data1[key] == data2[key]:
            proc_diff.add_unmodified(key, data2[key], diff)
        elif type_data:
            proc_diff.add_diff(key, diff, compare_data(data1[key], data2[key]))
        else:
            proc_diff.add_update(key, data1[key], data2[key], diff)

    return diff
