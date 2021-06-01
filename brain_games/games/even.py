import random

INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANDOM_RANGE = -10000
STOP_RANDOM_RANGE = 10000


def is_even(num):
    return num % 2 == 0


def generate_answer():
    question = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
