"""Here is the main loop of the brain algorithm"""

from random import randint
from .game import Game, ME
from .minimax import minimax, pruned_legal_moves


def generate_random_coordinates(length: int, height: int) -> tuple:
    """Generate a couple of (x, y) coordinates between 0 and length or height"""
    return randint(0, length - 1), randint(0, height - 1)

def evaluate(game: Game) -> tuple:
    print(game.board)
    """Returns the best position to play"""
    # x, y = win_coordinates(game.board, Players['ME'])
    # if x == -1:
    #     x, y = win_coordinates(game.board, Players['ENEMY'])
    legal_moves = pruned_legal_moves(game.board)
    if not legal_moves:
        return generate_random_coordinates(game.board.length, game.board.height)
    return minimax(game.board, player=ME)
