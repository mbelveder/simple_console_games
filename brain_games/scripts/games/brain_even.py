import random
import sys

from brain_games.cli import welcome_user
import brain_games.engine as egn


def main():
    # print the welcome phrase and the rules
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_counter = 0
    # user needs to win 3 times in a row
    while correct_counter < 3:
        number = random.randint(1, 100)

        user_answer = egn.ask_question(number)

        # False if the number is even
        if bool(number % 2):
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        correct_counter = egn.check_condition(
            user_answer=user_answer,
            correct_answer=correct_answer,
            counter=correct_counter,
            username=username
        )

    print(f'Congratulations, {username}!')
    sys.exit()


if __name__ == '__main__':
    main()
