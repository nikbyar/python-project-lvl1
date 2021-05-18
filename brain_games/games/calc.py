import random


def calc():
    start_random_range = 0
    stop_random_range = 20
    random_integer = [
        random.randint(start_random_range, stop_random_range)
        for index in range(2)
    ]
    signs = (' + ', ' - ', ' * ')
    random_sign = random.choice(signs)
    random_expression_str = (
        str(random_integer[0]) + random_sign + str(random_integer[1])
    )
    if random_sign == ' + ':
        random_expression_int = random_integer[0] + random_integer[1]
    elif random_sign == ' - ':
        random_expression_int = random_integer[0] - random_integer[1]
    else:
        random_expression_int = random_integer[0] * random_integer[1]
    return random_expression_str, random_expression_int
