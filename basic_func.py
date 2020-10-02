def check_if_zero(num, value_to_inherit=0):
    if num == 0:
        return True
    else:
        value_to_inherit = num
        return value_to_inherit


def take_input_as_int(a):
    val = int(input(f'{a}\n'))
    return val


def take_input_as_float(a):
    val = float(input(f'{a}\n'))
    return val


def take_input(a):
    val = input(f'{a}\n')
    return val
