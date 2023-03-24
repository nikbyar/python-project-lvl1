import random

LOWER_BOUND = 1
UPPER_BOUND = 10
WELCOME = 'What is the result of the expression?'
SIGNS = ['+', '-', '*']
NUMBER_OF_RANDOM_NUMBERS_IN_EXPRESSION = 2


def calculate_answer(random_ints, random_sign):
    if random_sign == '+':
        result = random_ints[0] + random_ints[1]
    elif random_sign == '-':
        result = random_ints[0] - random_ints[1]
    elif random_sign == '*':
        result = random_ints[0] * random_ints[1]
    return str(result)


def generate_question_answer():
    random_ints = [random.randint(LOWER_BOUND, UPPER_BOUND)
                   for i in range(NUMBER_OF_RANDOM_NUMBERS_IN_EXPRESSION)]
    random_sign = random.choice(SIGNS)
    result = calculate_answer(random_ints, random_sign)

    question = f'{(random_ints[0])} {random_sign} {(random_ints[1])}'
    return question, result
