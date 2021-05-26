#!/usr/bin/env python3
"""
Вычислитель отличий.

Программа определяющая разницу между двумя структурами данных.
"""
from gendiff.generate_difference import generate_diff
from parser_gendiff import create_pars


def main():
    """Главная функция.

    Обработка параметров команднойй строки.
    И вывод результата.
    """
    pars = create_pars()
    print(generate_diff(
        pars.first_file.name,
        pars.second_file.name,
        pars.format,
    ),
    )


if __name__ == '__main__':
    main()
