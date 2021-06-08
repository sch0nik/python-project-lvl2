"""Инициалиация и парсинг командно строки."""
import argparse


def parse_args():
    """Создание парсера параметров.

    Returns:
        возвращает созданный парсер.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output',
    )

    return parser.parse_args()
