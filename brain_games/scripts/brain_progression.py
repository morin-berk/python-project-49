#!/usr/bin/env python3
from brain_games.consts import PROGRESSION_RULES
from brain_games.games.brain_progression import play_progression
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import get_name, play_rounds


def main():
    greet()
    name = get_name()
    print(PROGRESSION_RULES)
    play_rounds(play_progression, name)


if __name__ == '__main__':
    main()
