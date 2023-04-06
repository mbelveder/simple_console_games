import prompt
import random
import sys

from brain_games.cli import welcome_user


def main():
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_counter = 0
    while correct_counter < 3:
        number = random.randint(1, 100)

        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == 'yes':
            user_antianswer = 'no'
        else:
            user_antianswer = 'yes'

        if bool(number % 2) and user_answer == 'no':
            print('Correct!')
            correct_counter += 1
        elif not bool(number % 2) and user_answer == 'yes':
            print('Correct!')
            correct_counter += 1
        else:
            error_message = f"'{user_answer}' is wrong answer;(. "
            error_message += f"Correct answer was '{user_antianswer}'."
            print(error_message)

            print(f'Let\'s try again, {username}!')
            sys.exit()

    print(f'Congratulations, {username}!')
    sys.exit()


if __name__ == '__main__':
    main()