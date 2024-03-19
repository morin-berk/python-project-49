#!/usr/bin/env python3

from brain_games.games.brain_gcd import play_gcd
from brain_games.scripts.brain_games import greet


def main():
    greet()
    play_gcd()


if __name__ == '__main__':
    main()