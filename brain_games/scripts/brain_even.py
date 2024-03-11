from random import randrange
import prompt
from brain_games.cli import welcome_user
from .brain_games import greet


def play_even_num():
    """
    The game asks a player if a number is even or odd.
    If a player answers correctly 3 times, they win.
    """
    name = welcome_user()

    q_text = 'Question: '
    a_text = 'Your answer: '

    rounds = 3

    print('Answer "yes" if the number is even, otherwise answer "no"')

    while rounds > 0:
        rounds -= 1
        random_number = randrange(1, 1000)

        print(q_text + str(random_number))
        answer = prompt.string(a_text)

        if random_number % 2 == 0 and answer == "yes":
            print('Correct!')
        elif random_number % 2 != 0 and answer == "no":
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.)")
            print("Let's try again, " + name + "!")
            break

        if rounds == 0:
            print("Congratulations, " + name + "!")


def main():
    greet()
    play_even_num()


if __name__ == '__main__':
    main()
