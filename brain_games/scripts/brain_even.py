#!/usr/bin/env python3
from brain_games.games.brain_even import play_even_num
from .game_logic import play_rounds


def main():
    play_rounds(play_even_num)


if __name__ == '__main__':
    main()
