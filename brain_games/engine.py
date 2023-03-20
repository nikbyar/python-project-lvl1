import prompt

ROUNDS = 3


def engine(game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {name}!")
    print(game.WELCOME)
    question, right_answer = game.generate_question_answer()
    counter = 0
    while counter < ROUNDS:
        print(f'Question: {question[counter]}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer[counter]:
            print('Correct!')
            counter += 1
        elif answer != right_answer[counter]:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{right_answer[counter]}'.\n"
                  f"Let's try again, {name}!")
            break

    if counter == ROUNDS:
        print(f'Congratulations, {name}!')
