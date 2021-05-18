import random


def progression():
    print('What number is missing in the progression?')
    initial_term = random.randint(0, 10)
    dif = random.choice([random.randint(-5, -1), random.randint(1, 5)])
    member = initial_term
    progr = str(initial_term)
    hidden_member_ind = random.randint(1, 8)
    for ind in range(10):
        if ind < hidden_member_ind:
            member += dif
            member_after_hidden = member + 2 * dif
            progr += ' ' + str(member)
        elif ind == hidden_member_ind:
            progr += ' : ' + str(member_after_hidden)
        else:
            member_after_hidden += dif
            hidden_member = member_after_hidden - dif * (10 - hidden_member_ind)
            progr += ' ' + str(member_after_hidden)

    return progr, hidden_member
