"""Функции для сравнения двух словарей."""

import json

import yaml

from gendiff import processing_diff


def compare_data(data1, data2):
    key_data1 = list(data1.keys())
    key_data2 = list(data2.keys())

    diff = processing_diff.create_diff()
    for item_key1 in key_data1:
        # получение значений из словарей
        # get возвращает None, если такого ключа нет
        value_data1 = data1.get(item_key1)
        value_data2 = data2.get(item_key1)

        # возможны три варианта
        # такого ключа нет во втором словаре
        if value_data2 is None:
            processing_diff.add_delete(item_key1, value_data1, diff)

        # значения в словарях по этому ключу равны
        elif value_data1 == value_data2:
            key_data2.remove(item_key1)
            processing_diff.add_unmodified(item_key1, value_data1, diff)

        # вругих случаях значит что ключ есть и там и там, но значения разные
        else:
            key_data2.remove(item_key1)
            if type(value_data1) == dict and type(value_data2) == dict:
                tmp_diff = compare_data(value_data1, value_data2)
                processing_diff.add_diff(item_key1, diff, tmp_diff)
            else:
                processing_diff.add_delete(item_key1, value_data1, diff)
                processing_diff.add_add(item_key1, value_data2, diff)

    # дописывание остатка от второго списка
    for item_key2 in key_data2:
        processing_diff.add_add(item_key2, data2.get(item_key2), diff)

    return diff


def generate_diff(file1, file2, formatter):
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

    if formatter == 'stylish':
        return processing_diff.stylish(compare_data(file1, file2))
