import random

COMPOSITE_NUMBERS = (
    4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30,
)
INTRO = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    gcd = min(num1, num2)
    while gcd > 0:
        if (num1 % gcd == 0) and (num2 % gcd == 0):
            break
        gcd -= 1
    return gcd


def generate_answer():
    num1 = random.choice(COMPOSITE_NUMBERS)
    num2 = random.choice(COMPOSITE_NUMBERS)
    two_rand_int = f'{num1} {num2}'
    return two_rand_int, str(find_gcd(num1, num2))
