"""Функции для работы с JSON - файлами."""
import json


def generate_diff(file_path_one, file_path_two):
    """Находит различия между двумя файлами.

    Args:
        file_path_one: первый файл и путь к нему.
        file_path_two: второй файл и путь к нему.

    Returns:
        Возвращает различия между входными файлами.
    """
    file1 = json.load(open(file_path_one))  # noqa: WPS515
    file2 = json.load(open(file_path_two))  # noqa: WPS515

    list_file1 = list(file1.keys())
    list_file2 = list(file2.keys())

    result = ''
    for item_list1 in list_file1:
        if item_list1 in list_file2:
            list_file2.remove(item_list1)
            if file1.get(item_list1) != file2.get(item_list1):
                result += f'- {item_list1}: {file1.get(item_list1)}\n'
                result += f'+ {item_list1}: {file2.get(item_list1)}\n'
            else:
                result += f'  {item_list1}: {file1.get(item_list1)}\n'
        else:
            result += f'- {item_list1}: {file1.get(item_list1)}\n'
    for item_list2 in list_file2:
        result += f'+ {item_list2}: {file2.get(item_list2)}\n'

    return result
