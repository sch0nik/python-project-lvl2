"""Модуль для фораттера json."""
import json


def format_json(data):
    """Форматирование data в стиле формата json.

    Args:
        data: данные diff,

    Returns:
        Строка diff отформатированная в виде json.
    """
    return json.dumps(data, indent=2)
