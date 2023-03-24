import prompt

ROUNDS = 3


def run_game(game):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {name}!")
    print(game.WELCOME)
    counter = 0
    while counter < ROUNDS:
        question, right_answer = game.generate_question_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            counter += 1
        elif answer != right_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{right_answer}'.\n"
                  f"Let's try again, {name}!")
            break

    if counter == ROUNDS:
        print(f'Congratulations, {name}!')
