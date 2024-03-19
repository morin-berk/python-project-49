from random import randrange
from brain_games.cli import welcome_user
from brain_games.scripts.game_logic import check_player_answer
from brain_games.consts import PROGRESSION_RULES, MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


def play_progression():
    """
    The game asks a player to find a mission number
    in an arithmetic progression.
    If a player answers correctly 3 times, they win.
    """
    name = welcome_user()

    print(PROGRESSION_RULES)

    rounds = 0

    while -1 < rounds < 3:

        progression_len = randrange(5, 10)
        missing_el_index = randrange(0, progression_len - 1)
        progression_step = randrange(1, 10)
        first_el = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH - progression_step)
        progression = []

        for el in range(first_el,
                        first_el + progression_step * progression_len,
                        progression_step):
            progression.append(el)

        correct_answer = progression[missing_el_index]
        progression[missing_el_index] = '..'
        question_expression = ' '.join(map(str, progression))

        rounds = check_player_answer(correct_answer,
                                     name,
                                     question_expression,
                                     rounds
                                     )

        if rounds == 3:
            print(f"Congratulations, {name}!")
