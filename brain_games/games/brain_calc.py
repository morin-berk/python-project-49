from random import randrange, choice
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import check_player_answer
from brain_games.consts import CALC_RULES, MIN_RANGE_LENGTH, \
    MAX_RANGE_LENGTH, MATH_SIGNS


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
        rand_signs = choice(MATH_SIGNS)

        if rand_signs == '-':
            correct_answer = num1 - num2
        elif rand_signs == "+":
            correct_answer = num1 + num2
        else:
            correct_answer = num1 * num2

        question_expression = f'{str(num1)} ' \
                              f'{str(rand_signs)} {str(num2)}'

        rounds = check_player_answer(correct_answer,
                                     name,
                                     question_expression,
                                     rounds
                                     )

        if rounds == 3:
            print(f"Congratulations, {name}!")
