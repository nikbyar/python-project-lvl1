import random
from math import sqrt


LOWER_BOUND = 1
UPPER_BOUND = 100
WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return number > 1


def generate_question_answer():
    random_int = random.randint(LOWER_BOUND, UPPER_BOUND)
    if is_prime(random_int):
        answer = 'yes'
    else:
        answer = 'no'
    return random_int, answer
