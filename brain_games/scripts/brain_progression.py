#!/usr/bin/env python3
from brain_games.games import brain_progression
from brain_games.game_logic import play_rounds


def main():
    play_rounds(brain_progression)


if __name__ == '__main__':
    main()
