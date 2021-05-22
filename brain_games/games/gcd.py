import random

COMPOSITE_NUMBERS = (
    4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30,
)


def gcd():
    first_int = random.choice(COMPOSITE_NUMBERS)
    second_int = random.choice(COMPOSITE_NUMBERS)
    counter = min(first_int, second_int)
    greatest_common_divisor = min(first_int, second_int)
    while counter > 0 and greatest_common_divisor > 0:
        if (first_int % greatest_common_divisor == 0) \
                and (second_int % greatest_common_divisor == 0):
            break
        else:
            greatest_common_divisor -= 1
        counter -= 1
    return greatest_common_divisor, first_int, second_int


def answer_generator():
    gcd1, rand1, rand2 = gcd()
    intro = 'Find the greatest common divisor of given numbers.'
    two_rand_int = str(f'{rand1} {rand2}')
    return two_rand_int, str(gcd1), intro
