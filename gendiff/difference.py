"""Функции для сравнения двух словарей."""


def generate_diff(data1, data2):
    """Находит различия между двумя словарями.

    Args:
        data1: первый словарь.
        data2: второй словарь.

    Returns:
        Возвращает строку с различием между этими словарями.
        Строка отсортирована.
    """
    key_data1 = list(data1.keys())
    key_data1 = sorted(key_data1)

    key_data2 = list(data2.keys())
    key_data2 = sorted(key_data2)

    diff = ''
    for item_key1 in key_data1:

        value_data1 = data1.get(item_key1)
        value_data2 = data2.get(item_key1)

        if value_data2 is None:
            tmp_string = f'- {item_key1}: {value_data1}'
        elif value_data1 == value_data2:
            key_data2.remove(item_key1)
            tmp_string = f'  {item_key1}: {value_data1}'
        else:
            key_data2.remove(item_key1)
            tmp_string = (
                f'- {item_key1}: {value_data1}\n'
                f'+ {item_key1}: {value_data2}'
            )

        diff += tmp_string + '\n'

    for item_key2 in key_data2:
        diff += f'+ {item_key2}: {data2.get(item_key2)}\n'

    return f'{{\n{diff}}}'
