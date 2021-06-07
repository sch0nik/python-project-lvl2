"""Парсер файлов."""
import json

import yaml


def parser(file1, file2):
    """Парсер файлов."""
    name1 = file1.split('.')
    name1 = name1[-1]

    name2 = file2.split('.')
    name2 = name2[-1]

    if name1 == name2 == 'json':
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
        return file1, file2
    elif name1 == name2 == 'yaml' or name1 == name2 == 'yml':  # noqa: WPS514
        file1 = yaml.full_load(open(file1))
        file2 = yaml.full_load(open(file2))
        return file1, file2
    return None, None
