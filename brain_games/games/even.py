import random
from brain_games.engine import ROUNDS


FIRST_RANDOM = 1
LAST_RANDOM = 50
WELCOME = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_if_even(number):
    if number % 2 == 0:
        return True


def generate_question_answer():
    random_ints = [random.randint(FIRST_RANDOM, LAST_RANDOM)
                   for i in range(0, ROUNDS)]
    is_even = []
    for i in random_ints:
        if check_if_even(i):
            is_even.append('yes')
        else:
            is_even.append('no')
    return random_ints, is_even
