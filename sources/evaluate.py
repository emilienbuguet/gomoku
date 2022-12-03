"""This is where the evaluation function of our algorithm is implemented"""

from .game import Board, ME, ENEMY
from .dictionary import pattern_list


def check_line(line: str, pattern: str) -> bool:
    """Checks if pattern is in string

    Args:
        line (str): The line to check in
        pattern (str): The pattern to search
    """
    return pattern in line


def generate_right_diag(board: Board, node_x: int, node_y: int) -> str:
    """Generates the right diagonals for the current cell

    Args:
        board (Board): State of the game
        node_x (int): x coordinate of the current cell
        node_y (int): y coordinate of the current cell

    Returns:
        tuple: Both bidirectional diagonals

    """
    right_min_offset = min(10 if node_x >= 10 else node_x, 10 if node_y >= 10 else node_y)
    right_max_offset = min(10 if node_x < board.length - 10 else board.length - node_x - 1,
                           10 if node_y < board.height - 10 else board.height - node_y - 1)

    right_x = node_x - right_min_offset

    max_right_x = node_x + right_max_offset
    right_y = node_y - right_min_offset
    right_max_y = node_y + right_max_offset

    right = ""

    for row in range(right_y, right_max_y + 1):
        if right_x <= max_right_x:
            right = right + board[row][right_x]
            right_x += 1
    return right


def generate_left_diag(board: Board, node_x: int, node_y: int) -> str:
    """Generates the right diagonals for the current cell

    Args:
        board (Board): State of the game
        node_x (int): x coordinate of the current cell
        node_y (int): y coordinate of the current cell

    Returns:
        tuple: Both bidirectional diagonals

    """
    left_min_offset = min(10 if node_x < board.length - 10 else board.length - node_x - 1,
                          10 if node_y >= 10 else node_y)
    left_max_offset = min(10 if node_x >= 10 else node_x,
                          10 if node_y < board.height - 10 else board.height - node_y - 1)

    left_x = node_x + left_min_offset
    min_left_x = node_x - left_max_offset
    left_y = node_y - left_min_offset
    left_max_y = node_y + left_max_offset

    left = ""

    for row in range(left_y, left_max_y + 1):
        if left_x >= min_left_x:
            left = left + board[row][left_x]
            left_x -= 1
    return left


def generate_bidirectional_diags_coords(board: Board) -> tuple:
    """Generates the bidirectional diagonals for the current cell

    Args:
        board (Board): State of the game

    Returns:
        tuple: Both bidirectional diagonals
    """

    right = []
    left = []

    for row in range(board.height):
        right.append((row, row))
        left.append((board.height - row - 1, row))

    return right, left


def evaluate(board: Board) -> int:
    total = 0
    for row in board:
        for size in range(5):
            score_me = row.count(ME * size) ** 2 if ENEMY + ME * size + ENEMY not in row else 0
            score_enemy = row.count(ENEMY * size) ** 2 if ME + ENEMY * size + ME not in row else 0
            total += score_me - score_enemy

    for i in range(board.length):
        col = "".join([row[i] for row in board])
        for size in range(5):
            score_me = col.count(ME * size) ** 2 if ENEMY + ME * size + ENEMY not in col else 0
            score_enemy = col.count(ENEMY * size) ** 2 if ME + ENEMY * size + ME not in col else 0
            total += score_me - score_enemy

    right, left = generate_bidirectional_diags_coords(board)

    for cell in right:
        diag = generate_left_diag(board, cell[0], cell[1])
        for size in range(5):
            score_me = diag.count(ME * size) ** 2 if ENEMY + ME * size + ENEMY not in diag else 0
            score_enemy = diag.count(ENEMY * size) ** 2 if ME + ENEMY * size + ME not in diag else 0
            total += score_me - score_enemy
    for cell in left:
        diag = generate_right_diag(board, cell[0], cell[1])
        for size in range(5):
            score_me = diag.count(ME * size) ** 2 if ENEMY + ME * size + ENEMY not in diag else 0
            score_enemy = diag.count(ENEMY * size) ** 2 if ME + ENEMY * size + ME not in diag else 0
            total += score_me - score_enemy

    return total
