import prompt


def check_player_answer(correct_answer, name, question_expression, rounds):
    """
    Implementing a universal game logic.
    A func gets a random question,
    asks a question and collect a player`s answer.
    Every time a player answers correctly, num_correct_answers increases by one.
    If a player answers incorrectly, a game ends.
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
