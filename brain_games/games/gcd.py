import random
from brain_games.engine import ATTEMPTS


FIRST_RANDOM = 1
LAST_RANDOM = 100
WELCOME = 'Find the greatest common divisor of given numbers.'


def get_gcd(pair):
    gcd = '1'
    for j in range(min(pair[0], pair[1]), 1, -1):
        if pair[0] % j == 0:
            if pair[1] % j == 0:
                gcd = str(j)
                return gcd
    return gcd


def generate_question_answer():
    random_ints = [[random.randint(FIRST_RANDOM, LAST_RANDOM)
                    for i in range(0, 2)] for j in range(0, ATTEMPTS)]
    result = []
    for pair in random_ints:
        result.append(get_gcd(pair))

    question = [' '.join((map(str, j))) for j in random_ints]
    return question, result
