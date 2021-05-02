#!/usr/bin/env python3
"""
Вычислитель отличий.

Программа определяющая разницу между двумя структурами данных.
"""

import json

from gendiff.difference import generate_diff
from gendiff.parsing import create_pars


def main():
    pars = create_pars().parse_args()
    file1 = json.load(open(pars.first_file.name))
    file2 = json.load(open(pars.second_file.name))

    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
