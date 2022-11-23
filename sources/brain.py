from game import Game, ME, ENEMY, Board
from win import has_won
from random import randint
from copy import deepcopy
from minimax import minimax


def generate_random_coordinates(length: int, height: int) -> (int, int):
    return randint(0, length - 1), randint(0, height - 1)


def has_stone_nearby(board: Board, x: int, y: int) -> bool:
    top_left_x = x - 1 if x > 0 else x
    top_left_y = y - 1 if y > 0 else y
    bottom_right_x = x + 1 if x < board.length - 1 else x
    bottom_right_y = y + 1 if y < board.height - 1 else y

    for row in board[top_left_y:bottom_right_y + 1]:
        if ME in row[top_left_x:bottom_right_x + 1] \
                or ENEMY in row[top_left_x:bottom_right_x + 1]:
            return True
    return False


def pruned_legal_moves(board: Board) -> list:
    free_slots: iter = filter(lambda c: c is not None, list([
        (x, y) if board[y][x] == 0 else None for x in range(board.length) for y in range(board.height)
    ]))
    legal_moves = list()
    win_moves = list()
    for (x, y) in free_slots:
        if has_stone_nearby(board, x, y):
            legal_moves.append((x, y))
            new_board: Board = deepcopy(board)
            new_board[y][x] = ME
            if has_won(new_board, ME):
                win_moves.append((x, y))
            new_board[y][x] = ENEMY
            if has_won(new_board, ENEMY):
                win_moves.append((x, y))

    return win_moves if win_moves else legal_moves


def evaluate(game: Game) -> (int, int):
    # x, y = win_coordinates(game.board, Players['ME'])
    # if x == -1:
    #     x, y = win_coordinates(game.board, Players['ENNEMY'])
    legal_moves = pruned_legal_moves(game.board)
    if not legal_moves:
        return generate_random_coordinates(game.board.length, game.board.height)
    return minimax(game.board, legal_moves)
