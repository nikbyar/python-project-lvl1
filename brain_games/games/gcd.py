import random


def gcd():
    print('Find the greatest common divisor of given numbers.')
    composite_numbers = (
        4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30,
    )
    rand_int = [
        random.choice(composite_numbers) for index in range(2)
    ]

    counter = min(rand_int)
    greatest_common_divisor = min(rand_int)
    while counter > 0 and greatest_common_divisor > 0:
        if (rand_int[0] % greatest_common_divisor == 0) \
                and (rand_int[1] % greatest_common_divisor == 0):
            break
        else:
            greatest_common_divisor -= 1
        counter -= 1
    two_rand_int = str(
        '{a} {b}'.format(a=rand_int[0], b=rand_int[1]),
    )
    return two_rand_int, greatest_common_divisor
