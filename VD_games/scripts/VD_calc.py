import random

from VD_games import cli
from VD_games.engine import run


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    question = f'{num1} {operation} {num2}'

    return question, str(answer)


def get_rules():
    return 'What is the result of the expression?'


def get_user_name():
    return cli.get_user_name()


class CalculatorGame:
    get_question_and_answer = staticmethod(get_question_and_answer)
    get_rules = staticmethod(get_rules)
    get_user_name = staticmethod(get_user_name)


def main():
    run(CalculatorGame)


if __name__ == '__main__':
    main()
