import prompt
from brain_games.consts import MAX_ROUNDS


def greet_and_get_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def play_rounds(play_game):
    """
    If a player answers correctly 3 times in a row, they win.
    If a player answers incorrectly at least once, a game ends.
    """
    name = greet_and_get_name()
    game_rules = play_game.RULES
    print(game_rules)

    rounds = 0

    while rounds < MAX_ROUNDS:
        correct_answer, question_expression = play_game.play_game()
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
