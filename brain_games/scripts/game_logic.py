import prompt

from brain_games.consts import MAX_ROUNDS
from brain_games.games.brain_calc import CALC_RULES
from brain_games.games.brain_even import EVEN_RULES
from brain_games.games.brain_gcd import GCD_RULES
from brain_games.games.brain_prime import PRIME_RULES
from brain_games.games.brain_progression import PROGRESSION_RULES


def greet_and_get_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def select_rules(game):
    game = game.__name__
    match game:
        case "play_calc":
            return CALC_RULES
        case "play_even_num":
            return EVEN_RULES
        case "play_gcd":
            return GCD_RULES
        case "play_prime":
            return PRIME_RULES
        case "play_progression":
            return PROGRESSION_RULES


def play_rounds(play_game):
    """
    If a player answers correctly 3 times in a row, they win.
    If a player answers incorrectly at least once, a game ends.
    """
    name = greet_and_get_name()

    game_rules = select_rules(play_game)
    print(game_rules)

    rounds = 0

    while rounds < MAX_ROUNDS:
        correct_answer, question_expression = play_game()
        question = f'Question: {question_expression}'
        print(question)
        player_answer = prompt.string('Your answer: ')

        if player_answer == str(correct_answer):
            print('Correct!')
            rounds += 1
        else:
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.)")
            print(f"Let's try again, {name}!")
            return

        print(f"Congratulations, {name}!")
