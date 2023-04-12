import random as rnd
from brain_games.cli import welcome_user
import brain_games.engine as egn
import sys


def main():

        # print the welcome phrase and the rules
    username = welcome_user()
    print('What number is missing in the progression?')

    correct_counter = 0
    # user needs to win 3 times in a row
    while correct_counter < 3:

        start = rnd.randint(1, 100)
        step = rnd.randint(1, 10)
        n_elements = 10
        progression = list(range(start, start + step * n_elements, step))

        # mask random element
        correct_answer = rnd.choice(progression)
        mask = ['..' if x == correct_answer else x for x in progression]

        user_answer_str = egn.ask_question(
            question_subject=mask,
            unpack_question=True
        )

        egn.check_user_input(user_answer_str)
        user_answer = int(user_answer_str)

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
