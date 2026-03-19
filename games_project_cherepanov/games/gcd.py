import random


DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))
    return question, correct_answer


GAME = {
    "description": DESCRIPTION,
    "generate_round": generate_round,
}

