"""Функция для сравнения двух словарей."""

import json

import yaml
from gendiff import processing_diff
from gendiff.formatter_diff import format_json, format_plain, format_stylish


# def compare_data(data1, data2):
#     """Сравнение двух данных.
#
#     Логика работы:
#     - получаю списки ключей обоих списков
#     - проверяю каждый элемент первого списка на присутствие во втором
#     - в зависимости от результата записываю текущий в диф с нужной пометкой
#     - если такой ключ был во втором списке, то удаляю его из него
#     - в кконце, во втором списке остаются только те элменты,
#     которых не было в первом, либо ничего не остается
#     - записываю все что осталось от второго списка в дифф.
#     """
#     key_list1 = list(data1.keys())
#     key_list2 = list(data2.keys())
#
#     diff = processing_diff.create_diff()
#     for item1 in key_list1:
#         # получение значений из словарей
#         # get возвращает None, если такого ключа нет
#         value_data1 = data1.get(item1)
#         value_data2 = data2.get(item1)
#
#         is_type_value1 = isinstance(value_data1, dict)
#         is_type_value2 = isinstance(value_data2, dict)
#
#         # Два варианта, либо ключ из первого словаря есть во втором,
#         # либо нет
#         if item1 in key_list2:
#             # Если ключ есть то сравниваю содержимое
#             if value_data1 == value_data2:
#                 processing_diff.add_unmodified(item1, value_data1, diff)
#             else:
#                 # Если содержимое не равно, то надо проверить
#                 # что это за элементы, если оба словари,
#                 # то надо проверить их содержимое
#                 if is_type_value1 and is_type_value2:
#                     # заход на более нижний уровень рекурсии
#                     tmp_diff = compare_data(value_data1, value_data2)
#                     processing_diff.add_diff(item1, diff, tmp_diff)
#                 else:
#                     # Иначе просто записывает изменившееся и старое значение
#                     processing_diff.add_update(
#                         item1,
#                         value_data1,
#                         value_data2,
#                         diff,
#                     )
#             key_list2.remove(item1)
#         else:
#             # ключа из первого словаря нет во втором
#             processing_diff.add_delete(item1, value_data1, diff)
#
#     # дописывание остатка от второго списка
#     for item_key2 in key_list2:
#         processing_diff.add_add(item_key2, data2.get(item_key2), diff)
#
#     return diff


def compare_data(data1, data2):
    """Сравнение двух данных."""
    diff = processing_diff.create_diff()

    set_data1 = set(data1)
    set_data2 = set(data2)

    items_add = set_data2 - set_data1
    items_add = sorted(list(items_add))
    list(map(
        lambda element: processing_diff.add_add(element, data2[element], diff),
        items_add,
    ))

    items_remove = set_data1 - set_data2
    items_remove = sorted(list(items_remove))
    list(map(
        lambda element: processing_diff.add_delete(element, data1[element], diff),
        items_remove,
    ))

    items_rest = set_data1 & set_data2
    items_rest = sorted(list(items_rest))

    items_unmod = []
    items_update = []

    for item in items_rest:
        if data1[item] == data2[item]:
            items_unmod.append(item)
        else:
            items_update.append(item)

    list(map(
        lambda element: processing_diff.add_unmodified(element, data2[element], diff),
        items_unmod,
    ))

    for item in items_update:
        type_data = isinstance(data1[item], dict) and isinstance(data2[item], dict)
        if not type_data:
            processing_diff.add_update(item, data1[item], data2[item], diff)
        else:
            tmp_diff = compare_data(data1[item], data2[item])
            processing_diff.add_diff(item, diff, tmp_diff)

    return diff


def generate_diff(file1, file2, formatter):
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
        return format_plain(compare_data(file1, file2), [])
    elif formatter == 'json':
        return format_json(compare_data(file1, file2))
    return 'Не известный формат.'
