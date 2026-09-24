import math
import random

from VD_games import cli
from VD_games.engine import run


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f'{num1} {num2}'
    answer = str(math.gcd(num1, num2))

    return question, answer


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def get_user_name():
    return cli.get_user_name()


class GcdGame:
    get_question_and_answer = staticmethod(get_question_and_answer)
    get_rules = staticmethod(get_rules)
    get_user_name = staticmethod(get_user_name)


def main():
    run(GcdGame)


if __name__ == '__main__':
    main()
