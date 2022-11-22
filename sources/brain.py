from game import Game, Players, Board
from win import win_coordinates, has_won
from random import randint, choice
from copy import deepcopy


def generate_random_coordinates(length: int, height: int) -> (int, int):
    return randint(0, length - 1), randint(0, height - 1)


def minimax(game: Game) -> (int, int):
    # Génération d'un game tree sur une depth donnée
    legal_moves: list = []
    return generate_random_coordinates(game.board.length, game.board.height)


def pruned_legal_moves(board: Board) -> list:
    free_slots: iter = filter(lambda c: c is not None, list([
        (x, y) if board[y][x] == 0 else None for x in range(board.length) for y in range(board.height)
    ]))
    # TODO filter the boxes that are adjacent to already set stones
    return list()


def evaluate(game: Game) -> (int, int):
    x, y = win_coordinates(game.board, Players['ME'])
    if x == -1:
        x, y = win_coordinates(game.board, Players['ENNEMY'])
    free_slots = pruned_legal_moves(game.board)
    # TODO check if this is the beginning of the game, if yes play center or random
    winner = [-1, -1, ]
    while x < 0 and y < 0 or game.board.stones[y][x] != 0:
        for (x, y) in free_slots:
            x, y = minimax(game)
    return x, y
