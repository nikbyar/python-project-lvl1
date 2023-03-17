import random

FIRST_RANDOM = 1
LAST_RANDOM = 9
WELCOME = 'What number is missing in the progression?'
TERMS = 10
COUNTS = 3


def generate_question_answer():
    gaped_progressions_list = []
    answers_list = []
    for i in range(COUNTS):
        progression_start = random.randint(FIRST_RANDOM, LAST_RANDOM)
        diff = random.randint(FIRST_RANDOM, LAST_RANDOM)
        gap_index = random.randint(FIRST_RANDOM, LAST_RANDOM)

        full_progression = [progression_start]
        for term in range(TERMS - 1):
            full_progression.append(full_progression[term] + diff)

        answer = str(full_progression[gap_index])

        gaped_progression = full_progression[:]
        gaped_progression[gap_index] = '..'
        gaped_progression = " ".join([str(i) for i in gaped_progression])

        gaped_progressions_list.append(gaped_progression)
        answers_list.append(answer)
    return gaped_progressions_list, answers_list
