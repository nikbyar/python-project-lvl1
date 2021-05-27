import random

INTRO = 'What is the result of the expression?'
START_RANDOM_RANGE = 0
STOP_RANDOM_RANGE = 20
SIGNS = ('+', '-', '*')


def generate_expr(num1, num2, sign):
    if sign == '+':
        expr_result = num1 + num2
    elif sign == '-':
        expr_result = num1 - num2
    else:
        expr_result = num1 * num2
    return str(expr_result)


def generate_answer():
    first_int = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    second_int = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    random_sign = random.choice(SIGNS)
    expression = f'{first_int} {random_sign} {second_int}'
    return expression, generate_expr(first_int, second_int, random_sign)
