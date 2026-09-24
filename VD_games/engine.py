ROUNDS_COUNT = 3


def run(game):
    name = game.get_user_name()

    print(game.get_rules())

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_answer()

        print(f'Question: {question}')
        answer = input('Your answer: ')

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
