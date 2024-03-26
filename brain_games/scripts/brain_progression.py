#!/usr/bin/env python3
from brain_games.games.brain_progression import play_progression, \
    PROGRESSION_RULES
from brain_games.scripts.brain_games import greet
from brain_games.scripts.game_logic import play_rounds


def main():
    greet()
    print(PROGRESSION_RULES)
    play_rounds(play_progression)


if __name__ == '__main__':
    main()
