"""Here is the main loop of the brain algorithm"""

from random import randint
from .game import Game, ME
from .minimax import minimax, pruned_legal_moves


def generate_random_coordinates(length: int, height: int) -> tuple:
    """Generate a couple of (x, y) coordinates between 0 and length or height

    Args:
        length (int): Maximum value for x
        height (int): Maximum value for y

    Returns:
        tuple: A couple of random coordinates
    """
    return randint(0, length - 1), randint(0, height - 1)


def get_best_move(game: Game) -> tuple:
    """Returns the best position to play

    Args:
        game (Game): The current game object

    Returns:
        tuple: Coordinates of the best move to make
    """
    legal_moves = pruned_legal_moves(game.board)
    if not legal_moves:
        return generate_random_coordinates(game.board.length, game.board.height)
    return minimax(game.board, player=ME)
