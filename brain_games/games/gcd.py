import random

import prompt


def random_pair():
    composite_numbers = (
        4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30,
    )
    random_integer = [
        random.choice(composite_numbers) for index in range(2)
    ]

    counter = min(random_integer)
    greatest_common_divisor = min(random_integer)
    while counter > 0 and greatest_common_divisor > 0:
        if (random_integer[0] % greatest_common_divisor == 0) \
                and (random_integer[1] % greatest_common_divisor == 0):
            break
        else:
            greatest_common_divisor -= 1
        counter -= 1

    return random_integer[0], random_integer[1], greatest_common_divisor


def gcd():
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        integer1, integer2, greatest_common_divisor = random_pair()
        print('Question: {b} {c}'.format(b=integer1, c=integer2))
        # ответ игрока и условие, при которых ответ верен и неверен
        player_answer = prompt.string('Your answer: ')
        if player_answer == str(greatest_common_divisor):
            print('Correct!')
            counter += 1
        else:
            print(
                "'{c}' is wrong answer ;(. Correct answer was '{d}'".
                format(c=player_answer, d=greatest_common_divisor),
            )
            counter += 1
            print("Let's try again!")
            break
    if counter > 2:
        print('Congratulations!')
