import prompt

from brain_games.cli import welcome_user


def get_name():
    name = welcome_user()
    return name


def play_rounds(play_game):
    """
    If a player answers correctly 3 times in a row, they win.
    If a player answers incorrectly at least once, a game ends.
    """
    name = get_name()

    rounds = 0

    while -1 < rounds < 3:
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
            # a player loses and a game ends
            rounds = -1

        if rounds == 3:
            print(f"Congratulations, {name}!")
