#!/usr/bin/env python3
"""
Вычислитель отличий.

Программа определяющая разницу между двумя структурами данных.
"""

import argparse

from gendiff.generate_difference import generate_diff


def create_pars():
    """Создание парсера параметров."""
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
        default='stylish',
        help='set format of output',
    )

    return parser


def main():
    pars = create_pars().parse_args()
    print(generate_diff(
        pars.first_file.name,
        pars.second_file.name,
        pars.format,
    )
    )


if __name__ == '__main__':
    main()
