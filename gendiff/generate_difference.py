"""Функция для сравнения двух словарей."""
from gendiff.parser import parse
from gendiff.formatters import format
from gendiff.processing_diff.formation_diff import compare_data


def generate_diff(file1, file2, formatter='stylish'):
    """Основная функция генерирования diff.

    На вход получает строки, с именами файлов и вид вывода.
    """
    name1 = file1.split('.')
    name1 = name1[-1]
    name2 = file2.split('.')
    name2 = name2[-1]
    ext = ''
    if name1 == name2 == 'json':
        ext = 'json'
    elif name1 == name2 == 'yaml' or name1 == name2 == 'yml':
        ext = 'yaml'

    file1, file2 = parse(ext, file1, file2)
    if not file1 or not file2:
        return 'Не поддерживаемый тип файлов, либо разные форматы'

    diff = compare_data(file1, file2)
    return format(diff, formatter)
