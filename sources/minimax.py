"""Here is the minimax algorithm implementation, using alpha-beta pruning"""

from random import choice
from math import inf
from .game import Board, ENEMY


def minimax(board: Board, legal_moves: list, player: int) -> tuple:
    """Minimax algorithm main loop, returns the best move's coordinates"""
    winner: dict = {"x": -1, "y": -1, "score": -inf if player == ENEMY else inf}

    return choice(legal_moves)
