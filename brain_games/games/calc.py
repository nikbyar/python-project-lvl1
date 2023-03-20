import random
from brain_games.engine import ROUNDS


LOWER_BOUND = 1
UPPER_BOUND = 10
WELCOME = 'What is the result of the expression?'
SIGNS = ['+', '-', '*']


def generate_question_answer():
    random_ints = [[random.randint(LOWER_BOUND, UPPER_BOUND)
                    for i in range(0, 2)] for j in range(0, ROUNDS)]
    random_signs = random.choices(SIGNS, k=ROUNDS)
    result = []

    for i in range(0, ROUNDS):
        if random_signs[i] == '+':
            a = random_ints[i][0] + random_ints[i][1]
        elif random_signs[i] == '-':
            a = random_ints[i][0] - random_ints[i][1]
        elif random_signs[i] == '*':
            a = random_ints[i][0] * random_ints[i][1]
        result.append(str(a))

    question = [f'{(random_ints[i][0])} {random_signs[i]} '
                f'{(random_ints[i][1])}' for i in range(0, ROUNDS)]
    return question, result
