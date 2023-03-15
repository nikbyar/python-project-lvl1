import prompt
import random


FIRST_RANDOM = 1
LAST_RANDOM = 5
ATTEMPTS = 3


def rand_even():
    random_ints = [random.randint(FIRST_RANDOM, LAST_RANDOM),
                   random.randint(FIRST_RANDOM, LAST_RANDOM),
                   random.randint(FIRST_RANDOM, LAST_RANDOM)]
    is_even = []
    for i in random_ints:
        if i % 2 == 0:
            is_even.append('yes')
        else:
            is_even.append('no')
    return random_ints, is_even


def even():
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_numbers = rand_even()
    counter = 0
    while counter < ATTEMPTS:
        print(f'Question: {random_numbers[0][counter]}')
        answer = prompt.string('Your answer: ')
        if answer == random_numbers[1][counter]:
            print('Correct!')
            counter += 1
        elif answer != random_numbers[1][counter]:
            print(f"{answer} is wrong answer ;(. Correct answer was "
                  f"{random_numbers[1][counter]}.\n"
                  f"Let's try again, {name}")
            break

    if counter == ATTEMPTS:
        print(f'Congratulations, {name}!')
