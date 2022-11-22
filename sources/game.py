from enum import Enum

Players = Enum('Players', ['ME', 'ENNEMY'])


class Board:
    def __init__(self, length: int, height: int):
        self.length = int(length)
        self.height = int(height)
        self.stones = [[0 for _ in range(0, self.length)] for _ in range(0, self.height)]

    def __str__(self) -> str:
        result: str = ''
        for i in range(0, self.height):
            result += 'MESSAGE '
            for n in range(0, self.length):
                result += '_' if self.stones[i][n] == 0 else '1' if self.stones[i][n] == 1 else '2'
                result += ' '
            result += '\n' if i < self.height - 1 else ''
        return result

    def __getitem__(self, y: int) -> list:
        return self.stones[y]

    def __setitem__(self, key, value):
        self.stones[key] = value

    def load(self, lines: list):
        for line in lines:
            [x, y, value] = list(map(int, line.split(',')))
            self.stones[y][x] = value

    def add_stone(self, value: int, x: int, y: int):
        if x < 0 or x >= self.length or y < 0 or y >= self.height:
            raise ValueError("Out of bounds: (%d, %d)" % (x, y))
        self.stones[y][x] = value


class Game:
    def __init__(self):
        """Constructor"""
        self.board = Board(20, 20)

    def new_board(self, length: int, height: int):
        self.board = Board(length, height)

    def load_board(self, lines: list):
        self.board.load(lines)

    def new_turn(self, player: Players, x, y):
        self.board.add_stone(player.value, x, y)
