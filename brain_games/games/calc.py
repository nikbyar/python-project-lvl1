import random

import prompt


def random_expression():
    start_random_range = 0
    stop_random_range = 20
    random_integer = [
        random.randint(start_random_range, stop_random_range)
        for index in range(2)
    ]
    signs = (' + ', ' - ', ' * ')
    random_sign = random.choice(signs)
    random_expression_str = (
        str(random_integer[0]) + random_sign + str(random_integer[1])
    )
    if random_sign == ' + ':
        random_expression_int = random_integer[0] + random_integer[1]
    elif random_sign == ' - ':
        random_expression_int = random_integer[0] - random_integer[1]
    else:
        random_expression_int = random_integer[0] * random_integer[1]
    return random_expression_str, random_expression_int


def calc():
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        question, answer = random_expression()
        print('Question: {b}'.format(b=question))
        # ответ игрока и условие, при которых ответ верен и неверен
        player_answer = prompt.string('Your answer: ')
        if player_answer == str(answer):
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
