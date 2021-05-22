"""Функция для сравнения двух словарей."""

import json

import yaml

from formatter_diff import format_json
from formatter_diff import format_plain
from formatter_diff import format_stylish
from gendiff import processing_diff


def compare_data(data1, data2):
    key_list1 = list(data1.keys())
    key_list2 = list(data2.keys())

    diff = processing_diff.create_diff()
    for item1 in key_list1:
        # получение значений из словарей
        # get возвращает None, если такого ключа нет
        value_data1 = data1.get(item1)
        value_data2 = data2.get(item1)

        if item1 in key_list2:
            if value_data1 == value_data2:
                processing_diff.add_unmodified(item1, value_data1, diff)
            else:
                if type(value_data1) == dict and type(value_data2) == dict:
                    tmp_diff = compare_data(value_data1, value_data2)
                    processing_diff.add_diff(item1, diff, tmp_diff)
                else:
                    processing_diff.add_update(
                        item1,
                        value_data1, value_data2,
                        diff
                    )
            key_list2.remove(item1)
        else:
            processing_diff.add_delete(item1, value_data1, diff)

    # дописывание остатка от второго списка
    for item_key2 in key_list2:
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
        return format_stylish(compare_data(file1, file2))
    elif formatter == 'plain':
        return format_plain(compare_data(file1, file2))
    elif formatter == 'json':
        return format_json(compare_data(file1, file2))
