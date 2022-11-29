"""Here are all the functions that can be used to check the win conditions"""

from .game import Board


# def check_line(line: list, player: int) -> int:
#     for i in range(len(line) - 4):
#         own_stones: int = line[i : i + 5].count(player)
#         free_stones: int = line[i : i + 5].count(0)
#         if own_stones == 4 and free_stones == 1:
#             return i + line[i : i + 5].index(0)
#     return -1


def need_to_check_diag(board: Board, node_x: int, node_y: int, player: int) -> bool:
    """Checks if diagonals have to be checked for the current cell

    Args:
        board (Board): State of the game
        node_x (int): x coordinate of the current cell
        node_y (int): y coordinate of the current cell
        player (int): Player being checked

    Returns:
        bool: True if the diagonals have to be checked, False otherwise
    """
    if node_x > 0 and node_y > 0 and board[node_y - 1][node_x - 1] == player:
        if node_x < board.length - 1 and board[node_y - 1][node_x + 1] == 0:
            return True
        return False
    if (
        node_x < board.length - 1
        and node_y > 0
        and board[node_y - 1][node_x + 1] == player
    ):
        if node_x > 0 and board[node_y - 1][node_x - 1] == 0:
            return True
        return False
    return True


def has_won(board: Board, player: int) -> bool:
    """Checks if the player has won the game

    Args:
        board (Board): The state of the game
        player (int): either ME or ENEMY (1 or 2)

    Returns:
        bool: True if the player has won the game, False otherwise
    """

    def generate_diags(node_x: int, node_y: int) -> tuple:
        """Generates the diagonals for the current cell

        Args:
            node_x (int): x coordinate of the current cell
            node_y (int): y coordinate of the current cell

        Returns:
            tuple: A tuple containing the diagonals
        """
        right = ""
        left = ""
        if node_y < board.height - 5 and node_x < board.length - 5:
            right = "".join([board[node_y + i][node_x + i] for i in range(5)])
        if node_y < board.height - 5 and node_x >= 4:
            left = "".join([board[node_y + i][node_x - i] for i in range(5)])
        return right, left

    for row in board.stones:
        if str(player) * 5 in row:
            return True
    cols = ["".join([row[x] for row in board.stones]) for x in range(board.length)]
    for col in cols:
        if str(player) * 5 in col:
            return True
    for row in range(board.height):
        for col in range(board.length):
            if board[row][col] == player and need_to_check_diag(
                board, col, row, player
            ):
                (right, left) = generate_diags(col, row)
                if player * 5 == right or player * 5 == left:
                    return True

    return False
