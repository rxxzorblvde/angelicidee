import prompt

ROUNDS_COUNT = 3


def run(game):
    print("Welcome to the VD Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game["description"])

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game["generate_round"]()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

