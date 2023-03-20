import random
from brain_games.engine import ROUNDS


LOWER_BOUND = 1
UPPER_BOUND = 100
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
    random_ints = [[random.randint(LOWER_BOUND, UPPER_BOUND)
                    for i in range(0, 2)] for j in range(0, ROUNDS)]
    result = []
    for pair in random_ints:
        result.append(get_gcd(pair))

    question = [' '.join((map(str, j))) for j in random_ints]
    return question, result
