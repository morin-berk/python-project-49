#!/usr/bin/env python3
from brain_games.games.brain_prime import play_prime, PRIME_RULES
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import play_rounds


def main():
    greet()
    print(PRIME_RULES)
    play_rounds(play_prime)


if __name__ == '__main__':
    main()
