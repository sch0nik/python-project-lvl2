import gendiff.processing_diff as diff

BASE_TAB = 4


def shaping(value, tab):
    if value is True or value is False:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif type(value) == dict:
        keys = list(value.keys())
        keys = sorted(keys)
        result = ''
        for item in keys:
            result += f'{" " * (tab  + BASE_TAB)}{item}: {shaping(value[item], tab + 4)}\n'
        result = f'{{\n{result}{" " * tab}}}'
        return result
    return str(value)


def stylish(data, tab=4):
    result = ''

    data = diff.sort_alphabetically(data)
    for item in data:
        name = diff.get_name(item)
        if diff.is_node(item):
            result += (
                f"{' '.rjust(tab)}"
                f"{name}: "
                f"{stylish(diff.get_children(item), 4 + tab)}\n"
            )
        else:
            current_state = diff.get_state(item)
            value = shaping(diff.get_value(item), tab)
            old_value = shaping(diff.get_old_value(item), tab)
            tmp = f'{name}: {value}\n'
            tmp_old = f'{name}: {old_value}\n'

            if current_state == diff.STATE_ADD:
                result += f"{'+ '.rjust(tab)}{tmp}"

            elif current_state == diff.STATE_UPDATE:
                result += f"{'- '.rjust(tab)}{tmp_old}"
                result += f"{'+ '.rjust(tab)}{tmp}"

            elif current_state == diff.STATE_REMOVE:
                result += f"{'- '.rjust(tab)}{tmp}"

            elif current_state == diff.STATE_UNMODIFIED:
                result += f"{'  '.rjust(tab)}{tmp}"

    result = f'{{\n{result}{" " * (tab-4)}}}'
    return result
