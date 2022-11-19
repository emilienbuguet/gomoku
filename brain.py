"""This is where the brain algorithm is implemented"""
from game import Game
from random import randint


def evaluate(game: Game) -> (int, int):
    x: int = randint(0, game.board.length - 1)
    y: int = randint(0, game.board.height - 1)
    return x, y
