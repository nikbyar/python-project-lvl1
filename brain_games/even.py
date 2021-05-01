import random
import prompt

start_random_range = -10000
stop_random_range = 10000
random_integer = [
    random.randint(start_random_range, stop_random_range) for ind in range(3)
]


def even_answer():
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print('Hello, {a}!'.format(a=player_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 0
    counter = 0
    while counter < 3:
        print('Question: {b}'.format(b=random_integer[index]))
        # ответ игрока и условия, при которых ответ верен и неверен
        answer = prompt.string('Your answer: ')
        correct_answer_yes = (random_integer[index] % 2 == 0)
        correct_answer_no = (random_integer[index] % 2 != 0)
        if (answer == 'yes') and correct_answer_yes:
            print('Correct!')
            counter += 1
            index += 1
        elif (answer == 'no') and correct_answer_no:
            print('Correct!')
            counter += 1
            index += 1
        else:
            # верный ответ
            correct_answer = 'yes' if correct_answer_yes else 'no'
            print(
                "'{c}' is wrong answer ;(. Correct answer was '{d}'".
                format(c=answer, d=correct_answer),
            )
            print("Let's try again, {e}!".format(e=player_name))
            break
    if counter > 2:
        print('Congratulations, {e}!'.format(e=player_name))


def main():
    even_answer()


if __name__ == 'main':
    main()
