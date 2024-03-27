#!/usr/bin/env python3
from brain_games.games.brain_gcd import play_gcd
from brain_games.scripts.game_logic import play_rounds


def main():
    play_rounds(play_gcd)


if __name__ == '__main__':
    main()
