import prompt


def engine():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=player_name))
