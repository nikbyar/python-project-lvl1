import random


def even_answer():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start_random_range = -10000
    stop_random_range = 10000
    random_integer = random.randint(start_random_range, stop_random_range)
    if random_integer % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return random_integer, answer
