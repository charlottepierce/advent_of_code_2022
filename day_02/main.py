#!/usr/bin/env python3

from enum import Enum


class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcomes(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


STRATEGY_GUIDE_CODES = {
    "A" : Moves.ROCK,
    "B" : Moves.PAPER,
    "C" : Moves.SCISSORS,
    "X" : Moves.ROCK,
    "Y" : Moves.PAPER,
    "Z" : Moves.SCISSORS
}


def _game_outcome(opponent_move, move):
    if opponent_move is move:
        return Outcomes.DRAW

    if (((move is Moves.ROCK) and (opponent_move is Moves.SCISSORS)) 
        or ((move is Moves.PAPER) and (opponent_move is Moves.ROCK)) 
        or ((move is Moves.SCISSORS) and (opponent_move is Moves.PAPER))):
        return Outcomes.WIN

    return Outcomes.LOSS


if __name__ == "__main__":
    score = 0
    with open("input.txt", 'r') as f:
        for line in f:
            opponent_move, my_move = [STRATEGY_GUIDE_CODES[m] for m in line.strip().split(" ")]

            score += my_move.value
            score += _game_outcome(opponent_move, my_move).value

    print("Part 1:", score)