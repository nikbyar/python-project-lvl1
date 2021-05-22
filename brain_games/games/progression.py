import random

START_RANDOM_RANGE = 0
STOP_RANDOM_RANGE = 10


def progression(start, length, step):
    member = start
    progr = str(start)
    hidden_member_ind = random.randint(1, length - 2)
    for ind in range(length):
        if ind < hidden_member_ind:
            member += step
            member_after_hidden = member + 2 * step
            progr += ' ' + str(member)
        elif ind == hidden_member_ind:
            progr += ' .. ' + str(member_after_hidden)
        else:
            member_after_hidden += step
            hidden_m = member_after_hidden - step * (length - hidden_member_ind)
            progr += ' ' + str(member_after_hidden)

    return progr, str(hidden_m)


def answer_generator():
    intro = 'What number is missing in the progression?'
    initial_term = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    dif = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    progr_length = 10
    output1, output2 = progression(initial_term, progr_length, dif)
    return output1, output2, intro
