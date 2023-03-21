import random
from brain_games.engine import ROUNDS

LOWER_BOUND = 1
UPPER_BOUND = 10
WELCOME = 'What number is missing in the progression?'
TERMS = 10


def generate_progression(first_term, common_diff, n):
    progression = [first_term]
    for term in range(n - 1):
        progression.append(progression[term] + common_diff)
    return progression


def progression_to_str(progression, gap_index):
    gaped_progression = progression[:]
    gaped_progression[gap_index] = '..'
    gaped_progression = " ".join([str(i) for i in gaped_progression])
    return gaped_progression


def generate_question_answer():
    gaped_progressions_list = []
    answers_list = []
    for i in range(ROUNDS):
        first_term = random.randint(LOWER_BOUND, UPPER_BOUND)
        common_diff = random.randint(LOWER_BOUND, UPPER_BOUND)
        gap_index = random.randint(LOWER_BOUND, UPPER_BOUND)
        progression = generate_progression(first_term, common_diff, TERMS)
        gaped_progression = progression_to_str(progression, gap_index)
        answer = str(progression[gap_index])

        gaped_progressions_list.append(gaped_progression)
        answers_list.append(answer)
    return gaped_progressions_list, answers_list
