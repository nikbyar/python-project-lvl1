import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=player_name))

    counter = 0
    while counter < 3:
        question, answer = game()
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
            print("Let's try again, {e}!".format(e=player_name))
            break
    if counter > 2:
        print('Congratulations, {f}!'.format(f=player_name))
