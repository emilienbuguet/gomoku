"""This is where the brain algorithm is implemented"""
from game import Game, Board, Players
from random import randint


def generate_random_coordinates(length: int, height: int) -> (int, int):
    return randint(0, length - 1), randint(0, height - 1)


def evaluate(game: Game) -> (int, int):
    x: int = -1
    y: int = -1
    x, y = win_coordinates(game, Players['ME'])
    if x == -1:
        x, y = win_coordinates(game, Players['ENNEMY'])
    while x < 0 and y < 0 or game.board.stones[y][x] != 0:
        x, y = generate_random_coordinates(game.board.length, game.board.height)
    return x, y


def win_coordinates(game: Game, player: Players) -> (int, int):
    """Returns coordinates of the winning move for the given player.
    :returns: (x, y) or (-1, -1) if there is no winning move.
    """
    def check_line(line: list) -> int:
        """Checks if a row or col has a winning play"""
        for i in range(len(line) - 4):
            own_stones: int = line[i:i + 5].count(player.value)
            free_stones: int = line[i:i + 5].count(0)
            if own_stones == 4 and free_stones == 1:
                return i + line[i:i + 5].index(0)
        return -1

    def check_diag(board: Board, x: int, y: int, direction: str) -> (int, int):
        """Checks if a node is the beginning of a winning diagonal"""
        # Right diagonal
        begin_offset = min(x, y, 4) if direction == 'right' else min(board.length - x - 1, y, 4)
        end_offset = min(board.length - x - 1, board.height - y - 1, 4) if direction == 'right'\
            else min(x, board.height - y - 1, 4)
        if direction == 'right':
            diag = [board[y + i][x + i] for i in range(-begin_offset, end_offset + 1)]
        else:
            diag = [board[y + i][x - i] for i in range(-begin_offset, end_offset + 1)]
        idx = check_line(diag)
        if idx != -1:
            return x - begin_offset + idx if direction == 'right' else x + begin_offset - idx, y - begin_offset + idx
        # # Left Diagonal
        # offset = find_left_offset(board, x, y)
        # size = offset + 5
        # diag = [board[y + i][x - i] for i in range(5)]
        # idx = check_line(diag)
        # if idx != -1:
        #     print("MESSAGE Found winning stone at %d" % idx)
        #     return x - idx, y + idx
        return -1, -1

    for y in range(game.board.height):
        x = check_line(game.board[y])
        if x != -1:
            return x, y

    for x in range(game.board.length):
        col = [row[x] for row in game.board.stones]
        y = check_line(col)
        if y != -1:
            return x, y


    for row in range(game.board.height):
        for col in range(game.board.length):
            if game.board[row][col] == player.value:
                x, y = check_diag(board=game.board, x=col, y=row, direction='right')
                if x != -1 and y != -1:
                    return x, y
                x, y = check_diag(board=game.board, x=col, y=row, direction='left')
                if x != -1 and y != -1:
                    return x, y
    return -1, -1
