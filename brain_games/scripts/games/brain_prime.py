from brain_games.cli import welcome_user
import random as rnd
import brain_games.engine as egn
from math import isqrt
import sys


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return 'no'
    limit = isqrt(n)
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return 'no'
    return 'yes'


def main():

    # print the welcome phrase and the rules
    username = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_counter = 0
    # user needs to win 3 times in a row
    while correct_counter < 3:

        number = rnd.randint(2, 1000)
        # print(number)
        # print()

        # use only odd numbers to make the game less trivial
        while number % 2 == 0:
            number = rnd.randint(2, 1000)
            # print(number)
            # print()

        user_answer_str = egn.ask_question(question_subject=number)
        correct_answer = is_prime(number)

        correct_counter = egn.check_condition(
            user_answer=user_answer_str,
            correct_answer=correct_answer,
            counter=correct_counter,
            username=username
        )

    print(f'Congratulations, {username}!')
    sys.exit()


if __name__ == '__main__':
    main()
