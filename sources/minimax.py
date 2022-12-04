"""Here is the minimax algorithm implementation, using alpha-beta pruning"""
import random
from copy import deepcopy
from math import inf
from .game import Board, ENEMY, ME
from .win import has_won
from .evaluate import evaluate

MAX_DEPTH = 3


def get_score(board: Board) -> int:
    """Returns the score of a move

    Args:
        board (Board): Current state of the game

    Returns:
        int: Score of the current board
    """
    score = random.randint(0, 100)
    return score


def has_stone_nearby(board: Board, node_x: int, node_y: int) -> bool:
    """Checks if a node of the board has a stone around it

    Args:
    board (Board): The current state of the game
    node_x (int): X coordinate of the node to check
    node_y (int): Y coordinate of the node to check

    Returns:
    bool: True if node has stones nearby, False otherwise
    """
    top_left_x = node_x - 1 if node_x > 0 else node_x
    top_left_y = node_y - 1 if node_y > 0 else node_y
    bottom_right_x = node_x + 1 if node_x < board.length - 1 else node_x
    bottom_right_y = node_y + 1 if node_y < board.height - 1 else node_y

    for row in board[top_left_y: bottom_right_y + 1]:
        if (
            ME in row[top_left_x: bottom_right_x + 1]
            or ENEMY in row[top_left_x: bottom_right_x + 1]
        ):
            return True
    return False


def pruned_legal_moves(board: Board) -> list:
    """Filters the board to keep the interesting nodes and send them back, so they can be treated

    Args:
    board (Board): The current state of the game

    Returns:
    list: A list of tuples containing all the playable coordinates
    """
    free_slots = filter(
        lambda c: c is not None,
        [
            (x, y) if board[y][x] == "0" else None
            for x in range(board.length)
            for y in range(board.height)
        ],
    )
    legal_moves = []
    win_moves = []
    if has_won(board, ME) or has_won(board, ENEMY):
        return []
    for (col, row) in free_slots:
        if has_stone_nearby(board, col, row):
            legal_moves.append((col, row))
            new_board: Board = deepcopy(board)
            line = list(new_board[row])
            line[col] = ME
            new_board[row] = line
            if has_won(new_board, ME):
                win_moves.append((col, row))
            line[col] = ENEMY
            new_board[row] = line
            if has_won(new_board, ENEMY):
                win_moves.append((col, row))

    return win_moves if win_moves else legal_moves


def update_legal_moves(x: int, y: int, board: Board) -> list:
    round_moves = [
        (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
        (x - 1, y), (x + 1, y),
        (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
    ]
    new_moves = []

    for move in round_moves:
        if move[0] < 0 or move[1] < 0:
            continue
        if move[0] > board.length - 1 or move[1] > board.height - 1:
            continue
        if board[move[1]][move[0]] != "0":
            continue
        new_moves.append(move)
    return new_moves

#
# def downgrade_legal_moves(x: int, y: int, legal_moves: list):
#     old_moves = [
#         (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
#         (x - 1, y), (x + 1, y),
#         (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
#     ]
#     for move in old_moves:
#         if move in legal_moves:
#             del legal_moves[legal_moves.index(move)]


def minimax(board: Board, begin_legal_moves: list) -> tuple:
    """Minimax algorithm main loop, returns the best move's coordinates"""

    def minimax_recur(depth: int, player: str, legal_moves: list, prev_alphabeta: int) -> int:
        next_turn = ME if player == ENEMY else ENEMY
        alphabeta = inf if player == ENEMY else -inf

        for move in legal_moves:
            dup_board.add_stone(player, move[0], move[1])

            next_moves = update_legal_moves(move[0], move[1], dup_board)
            res = minimax_recur(depth - 1, next_turn, next_moves, alphabeta) if depth != 0\
                else evaluate(dup_board)
            if (player == ME and res >= alphabeta) \
                    or (player == ENEMY and res <= alphabeta):
                alphabeta = res
            if (player == ME and alphabeta >= prev_alphabeta)\
                    or (player == ENEMY and alphabeta <= prev_alphabeta):
                dup_board.add_stone('0', move[0], move[1])
                break

            dup_board.add_stone('0', move[0], move[1])
        return alphabeta

    best_move: tuple = begin_legal_moves[0]
    dup_board = deepcopy(board)
    alpha = -inf
    for begin in begin_legal_moves:
        dup_board.add_stone(ME, begin[0], begin[1])
        dup_moves = update_legal_moves(begin[0], begin[1], board)
        score = minimax_recur(MAX_DEPTH, ENEMY, dup_moves, alpha)
        if alpha <= score:
            alpha = score
            best_move = begin
        dup_board.add_stone('0', begin[0], begin[1])
    return best_move
