from game import ME, ENEMY, Board


def check_line(line: list, player: int) -> int:
    for i in range(len(line) - 4):
        own_stones: int = line[i:i + 5].count(player)
        free_stones: int = line[i:i + 5].count(0)
        if own_stones == 4 and free_stones == 1:
            return i + line[i:i + 5].index(0)
    return -1


def check_diag(board: Board, x: int, y: int, direction: str, player: int) -> (int, int):
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


def win_coordinates(board: Board, player: int) -> (int, int):
    for y in range(board.height):
        x = check_line(board[y], player)
        if x != -1:
            return x, y

    for x in range(board.length):
        col = [row[x] for row in board.stones]
        y = check_line(col, player)
        if y != -1:
            return x, y

    for row in range(board.height):
        for col in range(board.length):
            if board[row][col] == player:
                x, y = check_diag(board=board, x=col, y=row, direction='right', player=player)
                if x != -1 and y != -1:
                    return x, y
                x, y = check_diag(board=board, x=col, y=row, direction='left', player=player)
                if x != -1 and y != -1:
                    return x, y
    return -1, -1


def has_won(board: Board, player: int) -> bool:
    def need_to_check_diag(x: int, y: int) -> bool:
        if x > 0 and y > 0 and board[y - 1][x - 1] == player:
            if x < board.length - 1 and board[y - 1][x + 1] == 0:
                return True
            return False
        if x < board.length - 1 and y > 0 and board[y - 1][x + 1] == player:
            if x > 0 and board[y - 1][x - 1] == 0:
                return True
            return False
        return True

    def generate_diags(x: int, y: int) -> (list, list):
        right = list()
        left = list()
        if y < board.height - 5 and x < board.length - 5:
            right = [board[y + i][x + i] for i in range(5)]
        if y < board.height - 5 and x >= 4:
            left = [board[y + i][x - i] for i in range(5)]
        return right, left

    for row in board.stones:
        if str(player) * 5 in ''.join(list(map(str, row))):
            return True
    cols = [[row[x] for row in board.stones] for x in range(board.length)]
    for col in cols:
        if str(player) * 5 in ''.join(list(map(str, col))):
            return True
    for y in range(board.height):
        for x in range(board.length):
            if board[y][x] == player and need_to_check_diag(x, y):
                (right, left) = generate_diags(x, y)
                if [player] * 5 == right or [player] * 5 == left:
                    return True

    return False
