import prompt
import random


FIRST_RANDOM = 1
LAST_RANDOM = 10
WELCOME = 'What is the result of the expression?'
SIGNS = ['+', '-', '*']

def generate_question_answer():
    random_ints = [[random.randint(FIRST_RANDOM, LAST_RANDOM)
                    for i in range(0, 2)] for j in range(0, 3)]
    random_signs = random.choices(SIGNS, k=3)
    result = []

    for i in range(0, 3):
        if random_signs[i] == '+':
            a = random_ints[i][0] + random_ints[i][1]
        elif random_signs[i] == '-':
            a = random_ints[i][0] - random_ints[i][1]
        elif random_signs[i] == '*':
            a = random_ints[i][0] * random_ints[i][1]
        result.append(str(a))

    question = [f'{(random_ints[i][0])} {random_signs[i]} '
                f'{(random_ints[i][1])}' for i in range(0, 3)]
    return question, result