#!/usr/bin/env python3
from brain_games.consts import EVEN_RULES
from brain_games.games.brain_even import play_even_num
from .brain_games import greet
from .game_logic import play_rounds, get_name


def main():
    greet()
    name = get_name()
    print(EVEN_RULES)
    play_rounds(play_even_num, name)


if __name__ == '__main__':
    main()
