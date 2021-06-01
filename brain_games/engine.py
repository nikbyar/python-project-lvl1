import prompt

ATTEMPTS = 3


def run(game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}!')
    counter = 0
    print(game.INTRO)
    while counter < ATTEMPTS:
        question, answer = game.generate_answer()
        print(f'Question: {question}')
        # ответ игрока и условие, при которых ответ верен и неверен
        player_answer = prompt.string('Your answer: ')
        if player_answer == answer:
            print('Correct!')
            counter += 1
        else:
            print(
                f"'{player_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'",
            )
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')
