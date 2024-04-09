from random import randrange
from brain_games.consts import MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


RULES = 'What number is missing in the progression?'


def get_correct_answer_and_progression():
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

    return correct_answer, progression


def play_game():
    """
    The game asks a player to find a mission number
    in an arithmetic progression.
    """
    correct_answer, progression = get_correct_answer_and_progression()
    question_expression = ' '.join(map(str, progression))

    return correct_answer, question_expression
