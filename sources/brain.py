from game import Game, Players, Board
from win import win_coordinates, has_won
from random import randint, choice
from copy import deepcopy


def generate_random_coordinates(length: int, height: int) -> (int, int):
    return randint(0, length - 1), randint(0, height - 1)


def minimax(game: Game) -> (int, int):
    return generate_random_coordinates(game.board.length, game.board.height)


def evaluate(game: Game) -> (int, int):
    x, y = win_coordinates(game.board, Players['ME'])
    if x == -1:
        x, y = win_coordinates(game.board, Players['ENNEMY'])
    while x < 0 and y < 0 or game.board.stones[y][x] != 0:
        x, y = minimax(game)
    return x, y
