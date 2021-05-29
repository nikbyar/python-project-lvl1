import random

INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANDOM_RANGE = 2
STOP_RANDOM_RANGE = 50


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def generate_answer():
    random_integer = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    if is_prime(random_integer):
        answer = 'yes'
    else:
        answer = 'no'
    return random_integer, answer
