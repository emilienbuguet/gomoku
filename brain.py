"""This is where the brain algorithm is implemented"""
from game import Game, Players
from win import win_coordinates
from random import randint


def generate_random_coordinates(length: int, height: int) -> (int, int):
    return randint(0, length - 1), randint(0, height - 1)


def monte_carlo(game: Game) -> (int, int):
    return 0, 0


def evaluate(game: Game) -> (int, int):
    x: int = -1
    y: int = -1
    x, y = win_coordinates(game, Players['ME'])
    if x == -1:
        x, y = win_coordinates(game, Players['ENNEMY'])
    while x < 0 and y < 0 or game.board.stones[y][x] != 0:
        x, y = monte_carlo(game)
    return x, y
