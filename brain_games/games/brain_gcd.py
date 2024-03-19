from random import randrange
from math import gcd
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import check_player_answer
from brain_games.consts import GCD_RULES, MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


def play_gcd():
    """
    The game asks a player to find the greatest common divisor
    of given numbers.
    If a player answers correctly 3 times, they win.
    """
    name = welcome_user()

    print(GCD_RULES)

    rounds = 0

    while -1 < rounds < 3:
        first_num = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
        second_num = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
        question_expression = f'{str(first_num)} {str(second_num)}'

        correct_answer = gcd(first_num, second_num)

        rounds = check_player_answer(correct_answer,
                                     name,
                                     question_expression,
                                     rounds
                                     )

        if rounds == 3:
            print(f"Congratulations, {name}!")
