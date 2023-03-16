import random


FIRST_RANDOM = 1
LAST_RANDOM = 50
WELCOME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    random_ints = [random.randint(FIRST_RANDOM, LAST_RANDOM),
                   random.randint(FIRST_RANDOM, LAST_RANDOM),
                   random.randint(FIRST_RANDOM, LAST_RANDOM)]
    is_even = []
    for i in random_ints:
        if i % 2 == 0:
            is_even.append('yes')
        else:
            is_even.append('no')
    return random_ints, is_even
