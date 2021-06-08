"""Парсер файлов."""
import json

import yaml


def parse(ext, file1, file2):
    """Парсер файлов."""
    if ext == 'json':
        file1 = json.load(open(file1))
        file2 = json.load(open(file2))
        return file1, file2
    elif ext == 'yaml':  # noqa: WPS514
        file1 = yaml.full_load(open(file1))
        file2 = yaml.full_load(open(file2))
        return file1, file2
    return None, None
