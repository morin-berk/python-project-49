#!/usr/bin/env python3

from brain_games.consts import GCD_RULES
from brain_games.games.brain_gcd import play_gcd
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import get_name, play_rounds


def main():
    greet()
    name = get_name()
    print(GCD_RULES)
    play_rounds(play_gcd, name)


if __name__ == '__main__':
    main()
