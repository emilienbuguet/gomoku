"""This is where the evaluation function of our algorithm is implemented"""

from .game import Board
from .dictionary import pattern_list
from .win import need_to_check_diag


def check_line(line: str, pattern: str) -> bool:
    """Checks if pattern is in string

    Args:
        line (str): The line to check in
        pattern (str): The pattern to search
    """
    return pattern in line


def generate_bidirectional_diags(board: Board, node_x: int, node_y: int) -> tuple:
    """Generates the bidirectional diagonals for the current cell

    Args:
        board (Board): State of the game
        node_x (int): x coordinate of the current cell
        node_y (int): y coordinate of the current cell

    Returns:
        tuple: Both bidirectional diagonals
    """
    right_min_offset = min(5 if node_x >= 5 else node_x, 5 if node_y >= 5 else node_y)
    right_max_offset = min(5 if node_x < board.length - 5 else board.length - node_x - 1,
                           5 if node_y < board.height - 5 else board.height - node_y - 1)
    left_min_offset = min(5 if node_x < board.length - 5 else board.length - node_x - 1,
                          5 if node_y >= 5 else node_y)
    left_max_offset = min(5 if node_x >= 5 else node_x,
                          5 if node_y < board.height - 5 else board.height - node_y - 1)

    right_x = node_x - right_min_offset
    left_x = node_x + left_min_offset
    max_right_x = node_x + right_max_offset
    min_left_x = node_x - left_max_offset
    right_y = node_y - right_min_offset
    right_max_y = node_y + right_max_offset
    left_y = node_y - left_min_offset
    left_max_y = node_y + left_max_offset

    right = ""
    left = ""

    for row in range(right_y, right_max_y + 1):
        if right_x <= max_right_x:
            right = right + board[row][right_x]
            right_x += 1
    for row in range(left_y, left_max_y + 1):
        if left_x >= min_left_x:
            left = left + board[row][left_x]
            left_x -= 1
    return right, left


def is_pattern_in_board(pattern: str, board: Board, player: int) -> bool:
    """Checks if the given pattern figures in the board

    Args:
        pattern (str): Pattern as string
        board (Board): Current state of the game
        player (int): Player that is being checked

    Returns:
        bool: True if pattern is in the board, False otherwise
    """

    for row in board:
        if check_line(row, pattern):
            return True

    cols = ["".join([row[i] for row in board.stones]) for i in range(board.length)]
    for col in cols:
        if check_line(col, pattern):
            return True

    for row in range(board.height):
        for col in range(board.length):
            if board[row][col] == player and need_to_check_diag(
                board, col, row, player
            ):
                (right, left) = generate_bidirectional_diags(board, col, row)
                if pattern in right or pattern in left:
                    return True
    return False


def evaluate(board: Board, player: int) -> int:
    """Returns the value of a board for a player

    Args:
        board (Board): The state of the game
        player (int): either ME or ENEMY (1 or 2)

    Returns:
        int: The value of the given board for the given player
    """
    pattern_list.sort(key=lambda p: p["value"], reverse=True)
    for pattern in pattern_list:
        pattern_str = pattern["pattern"].replace("o", str(player)).replace("_", "0")
        if is_pattern_in_board(pattern_str, board, player):
            return pattern["value"]
        if not pattern["symm"] and is_pattern_in_board(
            pattern_str[::-1], board, player
        ):
            return pattern["value"]
    return 0
