import random
from brain_games.engine import ROUNDS


LOWER_BOUND = 1
UPPER_BOUND = 100
WELCOME = 'Find the greatest common divisor of given numbers.'
NUMBER_OF_RANDOM_NUMBERS = 2


def get_gcd(pair):
    a, b = pair
    while a and b > 0:
        if a >= b:
            a = a % b
        elif a < b:
            b = b % a
    return max(a, b)


def generate_question_answer():
    # random_ints = [[random.randint(LOWER_BOUND, UPPER_BOUND)
    #                 for i in range(0, 2)] for j in range(0, ROUNDS)]
    # создание списка через генератор списков

    random_ints = []
    for i in range(ROUNDS):
        question = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS):
            question.append(random.randint(LOWER_BOUND, UPPER_BOUND))
        random_ints.append(question)

    result = []
    for pair in random_ints:
        result.append(str(get_gcd(pair)))

    question = [' '.join((map(str, j))) for j in random_ints]
    return question, result
