import random


FIRST_RANDOM = 1
LAST_RANDOM = 10
WELCOME = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    random_ints = [[random.randint(FIRST_RANDOM, LAST_RANDOM)
                    for i in range(0, 2)] for j in range(0, 3)]
    result = []
    for pair in random_ints:
        gcd = '1'
        for j in range(min(pair[0], pair[1]), 1, -1):
            if pair[0] % j == 0:
                if pair[1] % j == 0:
                    gcd = str(j)
                    break
        result.append(gcd)

    question = [' '.join((map(str, j))) for j in random_ints]
    return question, result
