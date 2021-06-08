"""Парсер файлов."""
import json

import yaml


def parse(ext, file):
    """Парсер файлов."""
    file = open(file)
    if ext == 'json':
        data = json.load(file)
    elif ext == 'yaml' or ext == 'yml':  # noqa: WPS514
        data = yaml.full_load(file)
    else:
        return None
    file.close()
    return data
