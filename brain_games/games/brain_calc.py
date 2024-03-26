from random import randrange, choice
from brain_games.consts import MIN_RANGE_LENGTH, MAX_RANGE_LENGTH, MATH_SIGNS

CALC_RULES = 'What is the result of the expression?'


def get_correct_answer(rand_sign, num1, num2):
    if rand_sign == '-':
        correct_answer = num1 - num2
    elif rand_sign == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 * num2

    return correct_answer


def play_calc():
    """
    The game asks a player an answer to the simple
    arithmetical expression (+, - or *).
    """
    num1, num2 = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH), randrange(
        MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
    random_sign = choice(MATH_SIGNS)

    correct_answer = get_correct_answer(random_sign, num1, num2)
    question_expression = f'{str(num1)} ' \
                          f'{str(random_sign)} {str(num2)}'

    return correct_answer, question_expression
