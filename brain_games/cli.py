import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=name))


def main():
    welcome_user()


if __name__ == 'main':
    main()
