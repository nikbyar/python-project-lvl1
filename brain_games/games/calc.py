import random
from brain_games.engine import ROUNDS

LOWER_BOUND = 1
UPPER_BOUND = 10
WELCOME = 'What is the result of the expression?'
SIGNS = ['+', '-', '*']
NUMBER_OF_RANDOM_NUMBERS_IN_EXPRESSION = 2


def generate_question_answer():
    random_ints = []
    for i in range(ROUNDS):
        question = []
        for j in range(NUMBER_OF_RANDOM_NUMBERS_IN_EXPRESSION):
            question.append(random.randint(LOWER_BOUND, UPPER_BOUND))
        random_ints.append(question)

    random_signs = random.choices(SIGNS, k=ROUNDS)
    result_list = []

    for i in range(ROUNDS):
        if random_signs[i] == '+':
            result = random_ints[i][0] + random_ints[i][1]
        elif random_signs[i] == '-':
            result = random_ints[i][0] - random_ints[i][1]
        elif random_signs[i] == '*':
            result = random_ints[i][0] * random_ints[i][1]
        result_list.append(str(result))

    question = [f'{(random_ints[i][0])} {random_signs[i]} '
                f'{(random_ints[i][1])}' for i in range(ROUNDS)]
    return question, result_list
