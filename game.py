"""This file contains the implementation of the Game class"""


class Board:
    def __init__(self, length: int, height=-1):
        self.length = length
        self.height = length if height < 0 else height

    @staticmethod
    def load(self, lines: list):
        self.length = len(list[0])
        self.height = len(list)
        return board

    def __str__(self):
        i, n = 0, 0
        while n < length:
            print('_')
        while i < height:
            n = 0
            print('|')
            while n < length:
                print(' ')
            print('|')
        n = 0
        while n < length:
            print('_')


class Game:
    """Game class"""
    def __init__(self):
        """Constructor"""
        self.board = Board(20, 20)
        print(self.board)

    def new_board(self, length: int, height: int):
        """Creates an empty board of length x and height y"""
        self.board = Board(length, height)

    def load_board(self, list):
        self.board = Board.load(list)
