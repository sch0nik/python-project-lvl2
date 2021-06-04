"""Функция для сравнения двух словарей."""

import json

import yaml
from gendiff.formatters import format_json, format_plain, format_stylish
from gendiff.processing_diff.formation_diff import compare_data


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
