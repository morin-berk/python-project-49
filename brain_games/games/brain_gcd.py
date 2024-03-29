from random import randrange
from math import gcd
from brain_games.consts import MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


GCD_RULES = 'Find the greatest common divisor of given numbers.'


def play_gcd():
    """
    The game asks a player to find the greatest common divisor
    of given numbers.
    """
    num1, num2 = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH), randrange(
        MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
    question_expression = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)

    return correct_answer, question_expression
