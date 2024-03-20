from random import randrange, choice
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import check_player_answer
from brain_games.consts import CALC_RULES, MIN_RANGE_LENGTH, \
    MAX_RANGE_LENGTH, MATH_SIGNS


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
    If a player answers correctly 3 times, they win.
    """
    name = welcome_user()

    print(CALC_RULES)

    rounds = 0

    while -1 < rounds < 3:

        num1, num2 = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH), \
                     randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
        random_sign = choice(MATH_SIGNS)

        correct_answer = get_correct_answer(random_sign, num1, num2)

        question_expression = f'{str(num1)} ' \
                              f'{str(random_sign)} {str(num2)}'

        rounds = check_player_answer(correct_answer,
                                     name,
                                     question_expression,
                                     rounds
                                     )

        if rounds == 3:
            print(f"Congratulations, {name}!")
