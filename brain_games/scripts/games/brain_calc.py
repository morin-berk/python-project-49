from random import randrange, choice
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import game_logic


def play_calc():
    """
    The game asks a player an answer to the simple
    arithmetical expression (+, - or *).
    If a player answers correctly 3 times, they win.
    """
    name = welcome_user()

    rules = 'What is the result of the expression?'
    print(rules)

    rounds = 0

    while -1 < rounds < 3:

        first_num = randrange(1, 100)
        second_num = randrange(1, 100)
        rand_signs = choice(["+", "-", "*"])

        if rand_signs == '-':
            correct_answer = first_num - second_num
        elif rand_signs == "+":
            correct_answer = first_num + second_num
        else:
            correct_answer = first_num * second_num

        question_expression = f'{str(first_num)} ' \
                              f'{str(rand_signs)} {str(second_num)}'

        rounds = game_logic(correct_answer,
                            name,
                            question_expression,
                            rounds
                            )

        if rounds == 3:
            print(f"Congratulations, {name}!")


def main():
    greet()
    play_calc()


if __name__ == '__main__':
    main()
