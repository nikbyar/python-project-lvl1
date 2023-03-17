import random


FIRST_RANDOM = 1
LAST_RANDOM = 100
PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    random_int = [random.randint(FIRST_RANDOM, LAST_RANDOM)
                  for i in range(0, 3)]
    answer = []
    for i in random_int:
        if i in PRIME_NUMBERS:
            answer.append('yes')
        else:
            answer.append('no')
    question = [str(i) for i in random_int]
    return question, answer
