#!/usr/bin/env python3

from brain_games.games.brain_calc import play_calc
from brain_games.scripts.brain_games import greet


def main():
    greet()
    play_calc()


if __name__ == '__main__':
    main()