#!/usr/bin/env python
from brain_games.games import brain_calc
from brain_games.game_logic import play_rounds


def main():
    play_rounds(brain_calc)


if __name__ == '__main__':
    main()
