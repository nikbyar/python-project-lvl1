import random

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
    first_term = random.randint(LOWER_BOUND, UPPER_BOUND)
    common_diff = random.randint(LOWER_BOUND, UPPER_BOUND)
    gap_index = random.randint(LOWER_BOUND, UPPER_BOUND - 1)
    progression = generate_progression(first_term, common_diff, TERMS)
    gaped_progression = progression_to_str(progression, gap_index)
    answer = str(progression[gap_index])
    return gaped_progression, answer
