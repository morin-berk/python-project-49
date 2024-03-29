from random import randrange
from brain_games.consts import MIN_RANGE_LENGTH, MAX_RANGE_LENGTH


PRIME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_num):
    if random_num == 1:
        return False

    for el in range(2, int(random_num ** 0.5) + 1):
        if random_num % el == 0:
            return False
    return True


def play_prime():
    """
    The game asks a player whether a number is prime or not.
    If a player answers correctly 3 times, they win.
    """
    random_num = randrange(MIN_RANGE_LENGTH, MAX_RANGE_LENGTH)
    correct_answer = "yes" if is_prime(random_num) else "no"
    question_expression = str(random_num)

    return correct_answer, question_expression
