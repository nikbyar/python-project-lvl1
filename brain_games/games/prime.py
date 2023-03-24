import random
from math import sqrt
from brain_games.engine import ROUNDS


LOWER_BOUND = 1
UPPER_BOUND = 100
WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return number > 1


def generate_question_answer():
    random_int = [random.randint(LOWER_BOUND, UPPER_BOUND)
                  for i in range(0, ROUNDS)]
    answer = []
    for i in random_int:
        if is_prime(i):
            answer.append('yes')
        else:
            answer.append('no')
    question = [str(i) for i in random_int]
    return question, answer
