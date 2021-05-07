"""Функции для сравнения двух словарей."""

import json
import yaml


def low_bool(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    return value


def compare_dict(data1, data2):
    """Находит различия между двумя словарями.

    Логика работы такая:
    - создаются списки ключей сравниваемых списков
    - они сортируются
    - дальше в цикле берется каждый элемент из первого списка
      и проверяется на наличие во втором
    - в зависимости от результата добавляется тот или иной
      результат, при этом он удаляется из второго списка
    - в последнем цикле выводится то что осталось от второго списка

    Args:
        data1: первый словарь.
        data2: второй словарь.

    Returns:
        Возвращает строку с различием между этими словарями.
        Результат отсортирован по алфавиту.
    """
    # получение и сортировка списков ключей
    key_data1 = list(data1.keys())
    key_data1 = sorted(key_data1)

    key_data2 = list(data2.keys())
    key_data2 = sorted(key_data2)

    # результирующая строка, пока пустая
    diff = ''
    for item_key1 in key_data1:
        # получение значений из словарей
        # get возвращает None, если такого ключа нет
        value_data1 = data1.get(item_key1)
        value_data2 = data2.get(item_key1)

        # возможны три варианта
        # такого ключа нет во втором словаре
        if value_data2 is None:
            tmp_string = f'  - {item_key1}: {low_bool(value_data1)}'
        # значения в словарях по этому ключу равны
        elif value_data1 == value_data2:
            key_data2.remove(item_key1)
            tmp_string = f'    {item_key1}: {low_bool(value_data1)}'
        # вругих случаях значит что ключ есть и там и там, а значения разные
        else:
            key_data2.remove(item_key1)
            tmp_string = (
                f'  - {item_key1}: {low_bool(value_data1)}\n'
                f'  + {item_key1}: {low_bool(value_data2)}'
            )

        diff += tmp_string + '\n'

    # дописывание остатка от второго списка
    for item_key2 in key_data2:
        diff += f'  + {item_key2}: {low_bool(data2.get(item_key2))}\n'

    diff = f'{{\n{diff}}}'
    return diff


def generate_diff(file1, file2):
    name = file1.split('.')
    name = name[-1]

    if name == 'json':
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
    elif name == 'yaml' or name == 'yml':
        file1 = yaml.full_load(open(file1))
        file2 = yaml.full_load(open(file2))
    else:
        return 'Не поддерживаемый тип файлов'

    return compare_dict(file1, file2)
