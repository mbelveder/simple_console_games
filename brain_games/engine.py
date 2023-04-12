import prompt
import sys


def ask_question(question_subject):
    """
    Asks user a question and returns user's answer

    Args:
        question_subject: The subject of the question

    Returns:
        User's answer
    """

    print(f'Question: {question_subject}')
    user_answer = prompt.string('Your answer: ')

    return user_answer


def check_condition(user_answer, correct_answer, counter: int, username: str):
    """
    Compares user's answer with the correct answer and adds 1 to the couter
    if they are identical

    Args:
        user_answer: user's answer
        correct_answer: correct answer
        counter (int): counter of correct answers
        username (str): user's name

    Returns:
        int: counter
    """

    # add point if the answer is correct
    if user_answer == correct_answer:
        print('Correct!')
        counter += 1
    # print error if user answer is incorrect and exit the script
    else:
        error_message = f"'{user_answer}' is wrong answer;(. "
        error_message += f"Correct answer was '{correct_answer}'."
        print(error_message)

        print(f'Let\'s try again, {username}!')
        sys.exit()

    return counter
