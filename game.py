"""This file contains the implementation of the Game class"""
from enum import Enum

Players = Enum('Players', ['ME', 'ENNEMY'])


class Board:
    def __init__(self, length: int, height: int):
        self.length = int(length)
        self.height = int(height)
        self.stones = [[0 for i in range(0, self.length)] for n in range(0, self.height)]

    def __str__(self) -> str:
        result: str = ''
        for i in range(0, self.height):
            for n in range(0, self.length):
                result += '_' if self.stones[i][n] == 0 else '1' if self.stones[i][n] == 1 else '2'
                result += ' '
            result += '\n'
        return result

    def load(self, lines: list):
        """Loads a board from lines of the following format, ended by "DONE":

        [X],[Y],[field] where field is 1 (own stone) or 2 (opponent's stone)
        """
        self.length = len(list[0])
        self.height = len(list)
        return board

    def add_stone(self, value: int, x: int, y: int):
        if x < 0 or x >= self.length or y < 0 or y >= self.height:
            raise ValueError("Out of bounds: (%d, %d)" % (x, y))
        self.stones[y][x] = value


class Game:
    """Game class"""
    def __init__(self):
        """Constructor"""
        self.board = Board(0, 0)

    def new_board(self, length: int, height: int):
        """Creates an empty board of length x and height y"""
        self.board = Board(length, height)

    def load_board(self, list):
        self.board = self.board.load(list)

    def new_turn(self, player: Players, x, y):
        self.board.add_stone(player.value, x, y)
