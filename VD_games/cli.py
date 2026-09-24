import prompt


def get_user_name():
    return prompt.string('May I have your name? ')


def welcome_user():
    name = get_user_name()
    print(f'Hello, {name}!')
