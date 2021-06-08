"""Функция для сравнения двух словарей."""
from gendiff.formatters import formatting
from gendiff.parser import parse  # noqa: WPS347
from gendiff.processing_diff.formation_diff import compare_data


def generate_diff(file1, file2, formatter='stylish'):
    """Основная функция генерирования diff.

    На вход получает строки, с именами файлов и вид вывода.
    """
    ext = file1.split('.')
    ext = ext[-1]
    file1 = parse(ext, file1)

    ext = file2.split('.')
    ext = ext[-1]
    file2 = parse(ext, file2)

    if not file1 or not file2:
        return 'Не поддерживаемый тип файлов, либо разные форматы'

    diff = compare_data(file1, file2)
    return formatting(diff, formatter)
