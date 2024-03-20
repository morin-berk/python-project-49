import prompt

from brain_games.cli import welcome_user


def get_name():
    name = welcome_user()
    return name


def check_player_answer(correct_answer, name, question_expression, rounds):
    """
    Implementing a universal game logic.
    A func gets a random question,
    asks a question and collect a player`s answer.
    If a player answers correctly, num_correct_answers increases by one.
    If a player answers incorrectly, num_correct_answers decreases by one.
    """
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

    return rounds


def play_rounds(play_game, name):
    """
    If a player answers correctly 3 times in a row, they win.
    If a player answers incorrectly at least once, a game ends.
    """
    rounds = 0

    while -1 < rounds < 3:
        correct_answer, question_expression = play_game()
        rounds = check_player_answer(correct_answer, name,
                                     question_expression, rounds
                                     )

        if rounds == 3:
            print(f"Congratulations, {name}!")
