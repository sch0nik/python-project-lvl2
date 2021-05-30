"""Функция для сравнения двух словарей."""

import json

import yaml
from gendiff import processing_diff as proc_diff
from gendiff.formatter_diff import format_json, format_plain, format_stylish


def compare_data(data1, data2):
    """Сравнение двух данных."""
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


def generate_diff(file1, file2, formatter='stylish'):
    """Основная функция генерирования diff.

    На вход получает строки, с именами файлов и вид вывода.
    """
    name = file1.split('.')
    name = name[-1]

    if name == 'json':
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
    elif name == 'yaml' or name == 'yml':  # noqa: WPS514
        file1 = yaml.full_load(open(file1))
        file2 = yaml.full_load(open(file2))
    else:
        return 'Не поддерживаемый тип файлов'

    if formatter == 'stylish':
        return format_stylish(compare_data(file1, file2))
    elif formatter == 'plain':
        return format_plain(compare_data(file1, file2))
    elif formatter == 'json':
        return format_json(compare_data(file1, file2))
    return 'Не известный формат.'
