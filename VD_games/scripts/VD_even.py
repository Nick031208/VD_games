import random


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 100)

        print(f'Question: {number}')
        answer = input('Your answer: ')

        correct_answer = 'yes' if number % 2 == 0 else 'no'

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            return

        print('Correct!')

    print('Congratulations!')


if __name__ == '__main__':
    main()
