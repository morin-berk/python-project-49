#!/usr/bin/env python3
from brain_games.games.brain_gcd import play_gcd, GCD_RULES
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import play_rounds


def main():
    greet()
    print(GCD_RULES)
    play_rounds(play_gcd)


if __name__ == '__main__':
    main()
