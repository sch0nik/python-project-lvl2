#!/usr/bin/env python3
"""
Вычислитель отличий.

Программа определяющая разницу между двумя структурами данных.
"""
from gendiff.cli import pars_args
from gendiff.generate_difference import generate_diff


def main():
    """Главная функция.

    Обработка параметров командной строки.
    И вывод результата.
    """
    args = pars_args()
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            args.format,
        ),
    )


if __name__ == '__main__':
    main()
