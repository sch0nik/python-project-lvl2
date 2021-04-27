#!/usr/bin/env python3
"""
Вычислитель отличий.

Программа определяющая разницу между двумя структурами данных.
"""

import argparse


def main():
    """Мэйн."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument(
        'first_file',
    )
    parser.add_argument(
        'second_file',
    )
    pars = parser.parse_args()


if __name__ == '__main__':
    main()
