from random import choice
from game import Board, ME, ENEMY
from math import inf


def minimax(board: Board, legal_moves: list, player: int) -> (int, int):
    winner: dict = {"x": -1, "y": -1, "score": -inf if player == ENEMY else inf}

    return choice(legal_moves)
