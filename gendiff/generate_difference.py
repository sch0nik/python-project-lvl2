"""Функция для сравнения двух словарей."""
from gendiff.file_parser import parser
from gendiff.formatters import format_selection
from gendiff.processing_diff.formation_diff import compare_data


def generate_diff(file1, file2, formatter='stylish'):
    """Основная функция генерирования diff.

    На вход получает строки, с именами файлов и вид вывода.
    """
    file1, file2 = parser(file1, file2)
    if not file1 or not file2:
        return 'Не поддерживаемый тип файлов либо разные форматы'

    diff = compare_data(file1, file2)
    return format_selection(diff, formatter)
