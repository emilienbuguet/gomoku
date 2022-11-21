from game import Game, Players, Board


def check_line(line: list, player: Players) -> int:
    """Checks if a row or col has a winning play"""
    for i in range(len(line) - 4):
        own_stones: int = line[i:i + 5].count(player.value)
        free_stones: int = line[i:i + 5].count(0)
        if own_stones == 4 and free_stones == 1:
            return i + line[i:i + 5].index(0)
    return -1


def check_diag(board: Board, x: int, y: int, direction: str, player) -> (int, int):
    """Checks if a node is the beginning of a winning diagonal"""
    begin_offset = min(x, y, 4) if direction == 'right' else min(board.length - x - 1, y, 4)
    end_offset = min(board.length - x - 1, board.height - y - 1, 4) if direction == 'right' \
        else min(x, board.height - y - 1, 4)
    if direction == 'right':
        diag = [board[y + i][x + i] for i in range(-begin_offset, end_offset + 1)]
    else:
        diag = [board[y + i][x - i] for i in range(-begin_offset, end_offset + 1)]
    idx = check_line(diag, player)
    if idx != -1:
        return x - begin_offset + idx if direction == 'right' else x + begin_offset - idx, y - begin_offset + idx
    return -1, -1


def win_coordinates(game: Game, player: Players) -> (int, int):
    """Returns coordinates of the winning move for the given player.
    :returns: (x, y) or (-1, -1) if there is no winning move.
    """
    for y in range(game.board.height):
        x = check_line(game.board[y], player)
        if x != -1:
            return x, y

    for x in range(game.board.length):
        col = [row[x] for row in game.board.stones]
        y = check_line(col, player)
        if y != -1:
            return x, y

    for row in range(game.board.height):
        for col in range(game.board.length):
            if game.board[row][col] == player.value:
                x, y = check_diag(board=game.board, x=col, y=row, direction='right', player=player)
                if x != -1 and y != -1:
                    return x, y
                x, y = check_diag(board=game.board, x=col, y=row, direction='left', player=player)
                if x != -1 and y != -1:
                    return x, y
    return -1, -1
