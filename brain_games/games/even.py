import random


LOWER_BOUND = 1
UPPER_BOUND = 50
WELCOME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_question_answer():
    random_int = random.randint(LOWER_BOUND, UPPER_BOUND)
    if is_even(random_int):
        answer = 'yes'
    else:
        answer = 'no'
    return random_int, answer
