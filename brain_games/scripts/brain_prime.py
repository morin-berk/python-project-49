#!/usr/bin/env python3

from brain_games.consts import PRIME_RULES
from brain_games.games.brain_prime import play_prime
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import get_name, play_rounds


def main():
    greet()
    name = get_name()
    print(PRIME_RULES)
    play_rounds(play_prime, name)


if __name__ == '__main__':
    main()
