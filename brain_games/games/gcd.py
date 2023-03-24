import random

LOWER_BOUND = 1
UPPER_BOUND = 100
WELCOME = 'Find the greatest common divisor of given numbers.'
NUMBER_OF_RANDOM_NUMBERS = 2


def get_gcd(pair):
    a, b = pair
    while a and b > 0:
        if a >= b:
            a = a % b
        elif a < b:
            b = b % a
    return max(a, b)


def generate_question_answer():
    random_pair = [random.randint(LOWER_BOUND, UPPER_BOUND)
                   for i in range(NUMBER_OF_RANDOM_NUMBERS)]
    result = str(get_gcd(random_pair))
    question = ' '.join(map(str, random_pair))
    return question, result
