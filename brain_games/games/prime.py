import random


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start_random_range = 2
    stop_random_range = 50
    random_integer = random.randint(start_random_range, stop_random_range)
    divisor = random_integer - 1
    counter = 0
    while divisor > 1:
        if (random_integer % divisor == 0):
            counter += 1
        divisor -= 1
    if counter > 0:
        answer = 'no'
    else:
        answer = 'yes'
    return random_integer, answer
