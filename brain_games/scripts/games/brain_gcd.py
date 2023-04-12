import random
from brain_games.cli import welcome_user
import brain_games.engine as egn
import sys


def gcd(a, b):
    # find minimum of a and b
    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # return the gcd of a and b
    return result


def main():
    # print the welcome phrase and the rules
    username = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    correct_counter = 0
    # user needs to win 3 times in a row
    while correct_counter < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)

        user_answer_str = egn.ask_question(f'{num_1} {num_2}')

        egn.check_user_input(user_answer_str)

        user_answer = int(user_answer_str)

        # calculation of the correct answer

        correct_answer = gcd(num_1, num_2)

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
