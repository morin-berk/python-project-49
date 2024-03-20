from random import randrange
from brain_games.consts import MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


def play_even_num():
    """
    The game asks a player if a number is even or odd.
    If a player answers correctly 3 times, they win.
    """
    random_number = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
    question_expression = f'{str(random_number)}'
    correct_answer = "yes" if random_number % 2 == 0 else "no"

    return correct_answer, question_expression
