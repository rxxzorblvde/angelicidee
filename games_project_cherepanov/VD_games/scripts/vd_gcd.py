import prompt
import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print("Welcome to the VD Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        print(f"Question: {a} {b}")
        answer = prompt.string("Your answer: ")

        correct = str(gcd(a, b))

        if answer == correct:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

    