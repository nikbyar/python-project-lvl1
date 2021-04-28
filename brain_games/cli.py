import prompt


def welcome_user():
    print('Welcome to the Brain Games!)))')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def main():
    welcome_user()


if __name__ == 'main':
    main()
