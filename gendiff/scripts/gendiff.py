#!/usr/bin/env python3
"""
Вычислитель отличий.

Программа определяющая разницу между двумя структурами данных.
"""

import argparse

from gendiff.difference import generate_diff


def main():
    """Мэйн."""
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
    pars = parser.parse_args()
    print(generate_diff(pars.first_file.name, pars.second_file.name))


if __name__ == '__main__':
    main()
