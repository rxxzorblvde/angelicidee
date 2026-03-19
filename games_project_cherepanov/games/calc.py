import random


DESCRIPTION = "What is the result of the expression?"


def calculate(a, b, op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case _:
            return a * b


def generate_round():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(["+", "-", "*"])
    question = f"{a} {op} {b}"
    correct_answer = str(calculate(a, b, op))
    return question, correct_answer


GAME = {
    "description": DESCRIPTION,
    "generate_round": generate_round,
}

