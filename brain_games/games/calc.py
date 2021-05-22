import random

START_RANDOM_RANGE = 0
STOP_RANDOM_RANGE = 20


def answer_generator():
    intro = 'What is the result of the expression?'
    first_int = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    second_int = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    signs = (' + ', ' - ', ' * ')
    sign = random.choice(signs)
    expression_str = str(first_int) + sign + str(second_int)
    if sign == ' + ':
        expression_int = first_int + second_int
    elif sign == ' - ':
        expression_int = first_int - second_int
    else:
        expression_int = first_int * second_int
    return expression_str, str(expression_int), intro
