#!/usr/bin/env python3
"""
Вычислитель отличий.

Программа определяющая разницу между двумя структурами данных.
"""
from gendiff.generate_difference import generate_diff
from gendiff.parser import create_pars


def main():
    """Главная функция.

    Обработка параметров команднойй строки.
    И вывод результата.
    """
    pars = create_pars()
    print(
        generate_diff(
            pars.first_file,
            pars.second_file,
            pars.format,
        ),
    )


if __name__ == '__main__':
    main()
