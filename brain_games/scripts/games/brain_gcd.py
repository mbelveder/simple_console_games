import random
from brain_games.cli import welcome_user
import brain_games.engine as egn
import sys


def find_dividers(num: int):
    """
    Returns all dividers for a `num`

    Args:
        num (int): integer for which all divider should be found

    Returns:
        list: list of dividers for a `num`
    """

    num_divs = []
    for n in range(1, num + 1):
        if num % n == 0:
            num_divs.append(n)

    return num_divs


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

        # calculation of the correct answer
        num_1_dividers = find_dividers(num_1)
        print(num_1_dividers)
        num_2_dividers = find_dividers(num_2)
        print(num_2_dividers)

        div_intersection = set(num_1_dividers).intersection(num_2_dividers)
        print(div_intersection)
        print(max(div_intersection))


if __name__ == '__main__':
    main()
