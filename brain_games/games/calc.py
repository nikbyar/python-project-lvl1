import random

INTRO = 'What is the result of the expression?'
START_RANDOM_RANGE = 0
STOP_RANDOM_RANGE = 20
SIGNS = ('+', '-', '*')


def calculate(num1, num2, sign):
    if sign == '+':
        expr_result = num1 + num2
    elif sign == '-':
        expr_result = num1 - num2
    elif sign == '*':
        expr_result = num1 * num2
    return expr_result


def generate_answer():
    first_int = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    second_int = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    random_sign = random.choice(SIGNS)
    expression = f'{first_int} {random_sign} {second_int}'
    return expression, str(calculate(first_int, second_int, random_sign))
