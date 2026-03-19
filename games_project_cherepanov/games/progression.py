import random


DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_LENGTH = 10


def make_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = make_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer


GAME = {
    "description": DESCRIPTION,
    "generate_round": generate_round,
}

