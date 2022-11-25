"""Here is the main loop of the brain algorithm"""

from copy import deepcopy
from random import randint
from .game import Game, ME, ENEMY, Board
from .win import has_won
from .minimax import minimax


def generate_random_coordinates(length: int, height: int) -> tuple:
    """Generate a couple of (x, y) coordinates between 0 and length or height"""
    return randint(0, length - 1), randint(0, height - 1)


def has_stone_nearby(board: Board, node_x: int, node_y: int) -> bool:
    """Checks if a node of the board has a stone around it"""
    top_left_x = node_x - 1 if node_x > 0 else node_x
    top_left_y = node_y - 1 if node_y > 0 else node_y
    bottom_right_x = node_x + 1 if node_x < board.length - 1 else node_x
    bottom_right_y = node_y + 1 if node_y < board.height - 1 else node_y

    for row in board[top_left_y: bottom_right_y + 1]:
        if (
            ME in row[top_left_x : bottom_right_x + 1]
            or ENEMY in row[top_left_x : bottom_right_x + 1]
        ):
            return True
    return False


def pruned_legal_moves(board: Board) -> list:
    """Filters the board to keep the interesting nodes and send them back, so they can be treated"""
    free_slots = filter(
        lambda c: c is not None,
            [
                (x, y) if board[y][x] == 0 else None
                for x in range(board.length)
                for y in range(board.height)
            ]
    )
    legal_moves = []
    win_moves = []
    for (col, row) in free_slots:
        if has_stone_nearby(board, col, row):
            legal_moves.append((col, row))
            new_board: Board = deepcopy(board)
            new_board[row][col] = ME
            if has_won(new_board, ME):
                win_moves.append((col, row))
            new_board[row][col] = ENEMY
            if has_won(new_board, ENEMY):
                win_moves.append((col, row))

    return win_moves if win_moves else legal_moves


def evaluate(game: Game) -> tuple:
    """Returns the best position to play"""
    # x, y = win_coordinates(game.board, Players['ME'])
    # if x == -1:
    #     x, y = win_coordinates(game.board, Players['ENEMY'])
    legal_moves = pruned_legal_moves(game.board)
    if not legal_moves:
        return generate_random_coordinates(game.board.length, game.board.height)
    return minimax(game.board, legal_moves, player=ME)
