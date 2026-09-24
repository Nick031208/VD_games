import math
import random

from VD_games import cli
from VD_games.engine import run


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            return False

    return True


def get_question_and_answer():
    number = random.randint(1, 100)

    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'

    return question, answer


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_user_name():
    return cli.get_user_name()


def main():
    import sys

    run(sys.modules[__name__])


if __name__ == '__main__':
    main()
