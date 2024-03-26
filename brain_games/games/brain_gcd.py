from random import randrange
from math import gcd
from brain_games.consts import MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


GCD_RULES = 'Find the greatest common divisor of given numbers.'


def get_two_nums():
    num1, num2 = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH), randrange(
        MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
    return num1, num2


def play_gcd():
    """
    The game asks a player to find the greatest common divisor
    of given numbers.
    """
    num1, num2 = get_two_nums()
    question_expression = f'{str(num1)} {str(num2)}'
    correct_answer = gcd(num1, num2)

    return correct_answer, question_expression
