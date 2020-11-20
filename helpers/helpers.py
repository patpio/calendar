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


def parse_user_filter(key, val):
    if val:
        if key in ['start_time', 'duration']:
            try:
                parse_val = datetime.strptime(val, '%d/%m/%y') if key == 'start_time' else int(val)
            except ValueError:
                print("Wrong data format")
            else:
                return parse_val
        else:
            return val
    else:
        return None
