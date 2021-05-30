"""Функция для сравнения двух словарей."""

import json

import yaml
from gendiff import processing_diff as proc_diff
from gendiff.formatter_diff import format_json, format_plain, format_stylish


# Линтер ругался что в этой функции слишком много выражений.
# Я отключил проверку этого правила. Мне кажется что все норм )))
# Но возможно можно что-то сделать еще. Но пока не придумал.
def compare_data(data1, data2):  # noqa: WPS213
    """Сравнение двух данных."""
    # Логика работы:
    # - делаю множества ключей обоих списков
    # - получаю списки ключей для дальнейшей работы
    # - обрабатываю эти списки
    diff = proc_diff.create_diff()

    set_data1 = set(data1)
    set_data2 = set(data2)

    # Добавленные ключи есть только во втором множестве
    items_add = list(set_data2 - set_data1)
    # Удаленные ключи есть только в первом множестве
    items_remove = list(set_data1 - set_data2)
    # Это остальные ключи, за вычетом первых двух множеств
    items_rest = list(set_data1 & set_data2)

    # В этом блоке из списка оставшихся ключей получаю:
    items_unmod = []  # список ключей которые не изменились
    items_update = []  # список ключей значения которых изменились
    items_update_node = []  # список ключей, значения которых будут вложенные
    for item in items_rest:
        # Индикатор того что оба значения одновременно не являются словарями
        type_data = not (
            isinstance(data1[item], dict) and isinstance(data2[item], dict)
        )
        if data1[item] == data2[item]:
            # Раз значения равны значит доавляем элемент с список не измененных
            items_unmod.append(item)
        elif type_data:
            # судя по индикатору этот элемент
            # идет в список с изменными значениями
            items_update.append(item)
        else:
            # судя по индикатору этот элемент будет вложенным
            items_update_node.append(item)

    # В этом блоке прохожу по каждому получившемуся списку
    # и добавляю эти значения в diff соответствующей функцией
    # Добавленные элементы
    list(map(
        lambda element: proc_diff.add_add(element, data2[element], diff),
        items_add,
    ))
    # Удаленные элементы
    list(map(
        lambda element: proc_diff.add_delete(element, data1[element], diff),
        items_remove,
    ))
    # Неизмененные элементы
    list(map(
        lambda element: proc_diff.add_unmodified(element, data2[element], diff),
        items_unmod,
    ))
    # Измененные не вложенные элементы
    list(map(
        lambda element: proc_diff.add_update(
            element,
            data1[element],
            data2[element],
            diff,
        ),
        items_update,
    ))
    # Измененные вложенные элементы
    list(map(
        lambda element: proc_diff.add_diff(
            element,
            diff,
            compare_data(data1[element], data2[element]),
        ),
        items_update_node,
    ))

    return diff


def generate_diff(file1, file2, formatter='stylish'):
    """Основная функция генерирования diff.

    На вход получает строки, с именами файлов и вид вывода.
    """
    name = file1.split('.')
    name = name[-1]

    if name == 'json':
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
    elif name == 'yaml' or name == 'yml':  # noqa: WPS514
        file1 = yaml.full_load(open(file1))
        file2 = yaml.full_load(open(file2))
    else:
        return 'Не поддерживаемый тип файлов'

    if formatter == 'stylish':
        return format_stylish(compare_data(file1, file2))
    elif formatter == 'plain':
        return format_plain(compare_data(file1, file2))
    elif formatter == 'json':
        return format_json(compare_data(file1, file2))
    return 'Не известный формат.'
