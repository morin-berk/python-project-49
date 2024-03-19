#!/usr/bin/env python3

from brain_games.games.brain_prime import play_prime
from brain_games.scripts.brain_games import greet


def main():
    greet()
    play_prime()


if __name__ == '__main__':
    main()