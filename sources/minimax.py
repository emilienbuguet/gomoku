"""Here is the minimax algorithm implementation, using alpha-beta pruning"""
import random
from .game import Board, ENEMY, ME
from copy import deepcopy
from .win import has_won
from .evaluate import evaluate


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

    for row in board[top_left_y : bottom_right_y + 1]:
        if (
            ME in row[top_left_x : bottom_right_x + 1]
            or ENEMY in row[top_left_x : bottom_right_x + 1]
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
    for (col, row) in free_slots:
        if has_stone_nearby(board, col, row):
            legal_moves.append((col, row))
            new_board: Board = deepcopy(board)
            new_board[row] = new_board[row][:col] + ME + new_board[row][col + 1 :]
            if has_won(new_board, ME):
                win_moves.append((col, row))
            new_board[row] = new_board[row][:col] + ENEMY + new_board[row][col + 1 :]
            if has_won(new_board, ENEMY):
                win_moves.append((col, row))

    return win_moves if win_moves else legal_moves


def minimax(board: Board, player: int) -> tuple:
    """Minimax algorithm main loop, returns the best move's coordinates"""

    def minimax_recur(board: Board, last_move: tuple,  depth: int, player: int) -> dict:
        if depth == 0:
            return {"x": last_move[0], "y": last_move[1], "score": evaluate(board, player)}
        if has_won(board, ME):
            return {"x": last_move[0], "y": last_move[1], "score": 1000}
        if has_won(board, ENEMY):
            return {"x": last_move[0], "y": last_move[1], "score": -1000}
        legal_moves: list = pruned_legal_moves(board)
        if not legal_moves:
            return {"x": last_move[0], "y": last_move[1], "score": evaluate(board, player)}

        moves = []
        next_turn = ME if player == ENEMY else ENEMY
        for move in legal_moves:
            moves.append(minimax_recur(deepcopy(board), move, depth - 1, next_turn))
        if player == ME:
            return max(moves, key=lambda i: i['score'])
        else:
            return min(moves, key=lambda i: i['score'])

    best_move = minimax_recur(board, (0, 0), 3, ME)
    return best_move['x'], best_move['y']
