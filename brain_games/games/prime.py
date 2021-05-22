import random

START_RANDOM_RANGE = 2
STOP_RANDOM_RANGE = 50


def prime(integ):
    divisor = integ - 1
    counter = 0
    if integ < 2:
        is_prime = 'no'
        return is_prime
    while divisor > 1:
        if (integ % divisor == 0):
            counter += 1
        divisor -= 1
    if counter > 0:
        is_prime = 'no'
    else:
        is_prime = 'yes'
    return is_prime


def answer_generator():
    random_integer = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return random_integer, prime(random_integer), intro
