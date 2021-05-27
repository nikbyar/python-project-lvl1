import random

INTRO = 'What number is missing in the progression?'
START_RANDOM_RANGE = 0
STOP_RANDOM_RANGE = 10
PROGR_LENGTH = 10


def generate_progression(start, length, step):
    progression = []
    for ind in range(0, length):
        progression.append(str(start + ind * step))
    return progression


def generate_answer():
    start = random.randint(START_RANDOM_RANGE, STOP_RANDOM_RANGE)
    step = random.choice([random.randint(-5, -1), random.randint(1, 5)])  # noqa: WPS221
    hidden_member_index = random.randint(0, PROGR_LENGTH - 1)
    progression = generate_progression(start, PROGR_LENGTH, step)
    hidden_member = progression[hidden_member_index]
    progression[hidden_member_index] = '..'
    progression = ' '.join(progression)
    return progression, hidden_member
