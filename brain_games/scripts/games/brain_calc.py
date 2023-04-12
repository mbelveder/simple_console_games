import random
import operator
from brain_games.cli import welcome_user
import brain_games.engine as egn
import sys


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def main():
    # print the welcome phrase and the rules
    username = welcome_user()
    print('What is the result of the expression?')

    correct_counter = 0
    # user needs to win 3 times in a row
    while correct_counter < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 15)

        # choose random operator and create question
        chosen_oper = random.choice(list(operators.keys()))
        expression = f'{num_1} {chosen_oper} {num_2}'

        user_answer_str = egn.ask_question(expression)

        egn.check_user_input(user_answer_str)

        user_answer = int(user_answer_str)
        correct_answer = int(operators[chosen_oper](num_1, num_2))

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
