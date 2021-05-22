import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    counter = 0
    while counter < 3:
        question, answer, intro = game.answer_generator()
        print(intro)
        print(f'Question: {question}')
        # ответ игрока и условие, при которых ответ верен и неверен
        player_answer = prompt.string('Your answer: ')
        if player_answer == answer:
            print('Correct!')
            counter += 1
        else:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'".
                format(player_answer, answer),
            )
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')
