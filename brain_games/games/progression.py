import random

import prompt


def arifm_progression():
    initial_term = random.randint(0, 10)
    dif = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    member = initial_term
    progression = str(initial_term)
    hidden_member_ind = random.randint(1, 8)
    for ind in range(10):
        if ind < hidden_member_ind:
            member += dif
            member_after_hidden = member + 2 * dif
            progression += ' ' + str(member)
        elif ind == hidden_member_ind:
            progression += ' : ' + str(member_after_hidden)
        else:
            member_after_hidden += dif
            hidden_member = member_after_hidden - dif * (10 - hidden_member_ind)
            progression += ' ' + str(member_after_hidden)

    return progression, hidden_member


def progression():
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        progr, hidden_member = arifm_progression()
        print('Question: {b}'.format(b=progr))
        # ответ игрока и условие, при которых ответ верен и неверен
        player_answer = prompt.string('Your answer: ')
        if player_answer == str(hidden_member):
            print('Correct!')
            counter += 1
        else:
            print(
                "'{c}' is wrong answer ;(. Correct answer was '{d}'".
                format(c=player_answer, d=hidden_member),
            )
            counter += 1
            print("Let's try again!")
            break
    if counter > 2:
        print('Congratulations!')
