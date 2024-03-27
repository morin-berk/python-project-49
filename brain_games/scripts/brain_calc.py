#!/usr/bin/env python
from brain_games.games.brain_calc import play_calc
from brain_games.scripts.game_logic import play_rounds


def main():
    play_rounds(play_calc)


if __name__ == '__main__':
    main()
