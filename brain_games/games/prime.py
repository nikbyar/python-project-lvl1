import random

import prompt


def is_prime():
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


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        random_integer, answer = is_prime()
        print('Question: {b}'.format(b=random_integer))
        # ответ игрока и условие, при которых ответ верен и неверен
        player_answer = prompt.string('Your answer: ')
        if player_answer == answer:
            print('Correct!')
            counter += 1
        else:
            print(
                "'{c}' is wrong answer ;(. Correct answer was '{d}'".
                format(c=player_answer, d=answer),
            )
            counter += 1
            print("Let's try again!")
            break
    if counter > 2:
        print('Congratulations!')
