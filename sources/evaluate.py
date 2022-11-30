"""This is where the evaluation function of our algorithm is implemented"""

from .game import Board
from .dictionary import pattern_list


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


def static_eval(row: str, col: str, right: str, left: str, x: int, y: int, player: str) -> int:
    def get_static_index(line: str, default: int) -> int:
        while default > 0 and line[default - 1] == player:
            default -= 1
        return default

    def get_static_value_line(line: str, index: int) -> int:
        length = 0
        for i in line[index:]:
            if i == player:
                length += 1
            else:
                break
        return length

    def get_static_value_diag(line: str) -> int:
        length = 0
        for i in range(5):
            if player * i in line:
                length = i
            else:
                break
        return length

    row_index = get_static_index(row, x)
    col_index = get_static_index(col, y)
    return (get_static_value_line(row, row_index) + get_static_value_line(col, col_index) +
            get_static_value_diag(right) + get_static_value_diag(left))


def is_cell_in_pattern(pattern: str, board: Board, x: int, y: int, player: str) -> tuple:
    """Checks if the given pattern figures in the board

    Args:
        pattern (str): Pattern as string
        board (Board): Current state of the game
        x (int): X coordinate of the cell
        y (int): Y coordinate of the cell
        player (str): Player that is being checked

    Returns:
        bool: True if pattern is in the board, False otherwise
    """

    if check_line(board[y], pattern):
        return True, 0

    col = "".join([row[x] for row in board.stones])
    if check_line(col, pattern):
        return True, 0

    (right, left) = generate_bidirectional_diags(board, x, y)
    if check_line(right, pattern) or check_line(left, pattern):
        return True, 0
    return False, static_eval(board[y], col, right, left, x, y, player)


def evaluate(board: Board, player: str, x: int, y: int) -> int:
    """Returns the value of a board for a player

    Args:
        board (Board): The state of the game
        player (int): either ME or ENEMY (1 or 2)
        x (int): X coordinate of the node
        y (int) Y coordinate of the node

    Returns:
        int: The value of the given board for the given player
    """
    pattern_list.sort(key=lambda p: p["value"], reverse=True)
    row = board[y]
    col = "".join([row[x] for row in board.stones])
    (right, left) = generate_bidirectional_diags(board, x, y)
    for pattern in pattern_list:
        pattern_str = pattern["pattern"].replace("o", str(player)).replace("_", "0")
        if check_line(row, pattern_str) or check_line(col, pattern_str) or check_line(right, pattern_str) or \
           check_line(left, pattern_str):
            return pattern["value"]
        rev_pattern = pattern_str[::-1]
        if check_line(row, rev_pattern) or check_line(col, rev_pattern) or check_line(right, rev_pattern) or \
           check_line(left, rev_pattern):
            return pattern["value"]
    return static_eval(row, col, right, left, x, y, player)
