"""This is where the brain algorithm is implemented"""
from game import Game
from random import randint


def generate_random_coordinates(length: int, height: int) -> (int, int):
    return randint(0, length - 1), randint(0, height - 1)

def evaluate(game: Game) -> (int, int):
    x: int = -1
    y: int = -1
    while x >= 0 and y >= 0 and game.board.stones[x][y] != 0:
        x, y = generate_random_coordinates(length, height)
    return x, y
