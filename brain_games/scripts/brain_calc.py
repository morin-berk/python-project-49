#!/usr/bin/env python
from brain_games.games.brain_calc import play_calc, CALC_RULES
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import play_rounds


def main():
    greet()
    print(CALC_RULES)
    play_rounds(play_calc)


if __name__ == '__main__':
    main()
