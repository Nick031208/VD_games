import random

from VD_games import cli
from VD_games.engine import run


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    hidden_index = random.randint(0, length - 1)

    progression = []

    for index in range(length):
        current_element = start + index * step

        if index == hidden_index:
            progression.append('..')
        else:
            progression.append(str(current_element))

    question = ' '.join(progression)
    answer = str(start + hidden_index * step)

    return question, answer


def get_question_and_answer():
    return generate_progression()


def get_rules():
    return 'What number is missing in the progression?'


def get_user_name():
    return cli.get_user_name()

def main():
    import sys

    run(sys.modules[__name__])


if __name__ == '__main__':
    main()
