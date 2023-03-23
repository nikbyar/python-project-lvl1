import random
from brain_games.engine import ROUNDS


LOWER_BOUND = 1
UPPER_BOUND = 50
WELCOME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True


def generate_question_answer():
    random_ints = [random.randint(LOWER_BOUND, UPPER_BOUND)
                   for i in range(0, ROUNDS)]
    answer = []
    for i in random_ints:
        if is_even(i):
            answer.append('yes')
        else:
            answer.append('no')
    return random_ints, answer
