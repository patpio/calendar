def gen_id():
    idx = 0

    def inner():
        nonlocal idx

        result = idx
        idx += 1

        return result

    return inner


uuid = gen_id()
