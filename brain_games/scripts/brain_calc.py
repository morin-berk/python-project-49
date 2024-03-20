#!/usr/bin/env python
from brain_games.consts import CALC_RULES
from brain_games.games.brain_calc import play_calc
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import get_name, play_rounds


def main():
    greet()
    name = get_name()
    print(CALC_RULES)
    play_rounds(play_calc, name)


if __name__ == '__main__':
    main()
