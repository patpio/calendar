from datetime import datetime


def gen_id():
    idx = 0

    def inner():
        nonlocal idx

        result = idx
        idx += 1

        return result

    return inner


uuid = gen_id()


def parse_user_update(key, val):
    if key == 'duration':
        return int(val)
    else:
        return val


def parse_user_filter(key, val):
    if key in ['start_time', 'duration']:
        if val:
            return datetime.strptime(val, '%d/%m/%y') if key == 'start_time' else int(val)
        else:
            return None
    else:
        return val
