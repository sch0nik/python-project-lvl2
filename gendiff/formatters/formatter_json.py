"""Модуль для фораттера json."""
import json


def format_json(data):
    """Форматирование data в стиле формата json."""
    return json.dumps(data, indent=2)
