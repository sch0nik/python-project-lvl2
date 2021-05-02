"""Модуль для парсера параметров командной строки."""

import argparse


def create_pars():
    """
    Создание парсера параметров.

    Returns:
        Возвращается ссылка на соданный парсер.
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        'first_file',
        type=open,
    )
    parser.add_argument(
        'second_file',
        type=open,
    )
    parser.add_argument(
        '-f',
        '--format',
        default='FORMAT',
        help='set format of output',
    )

    return parser
