"""Here is the gomoku implementation without GUI"""

ME = 1
ENEMY = 2


class Board:
    """This is the state of the current running gomoku game"""

    def __init__(self, length: int, height: int):
        self.length = int(length)
        self.height = int(height)
        self.stones = [
            [0 for _ in range(0, self.length)] for _ in range(0, self.height)
        ]

    def __str__(self) -> str:
        result: str = ""
        for i in range(0, self.height):
            result += "MESSAGE "
            for j in range(0, self.length):
                result += (
                    "_"
                    if self.stones[i][j] == 0
                    else "1"
                    if self.stones[i][j] == 1
                    else "2"
                )
                result += " "
            result += "\n" if i < self.height - 1 else ""
        return result

    def __getitem__(self, i: int) -> list:
        return self.stones[i]

    def __setitem__(self, key, value):
        self.stones[key] = value

    def load(self, lines: list):
        """Loads a new board from a list of lines.

        Args:
            lines (list): Lines of the given format : x,y,value
        """
        for line in lines:
            [x_coordinate, y_coordinate, value] = list(map(int, line.split(",")))
            self.stones[y_coordinate][x_coordinate] = value

    def add_stone(self, value: int, stone_x: int, stone_y: int):
        """Adds a new stone to the board.

        Args:
            value (int): Value of the stone
            stone_x (int): X coordinate of the stone
            stone_y (int): Y coordinate of the stone
        """
        if (
            stone_x < 0
            or stone_x >= self.length
            or stone_y < 0
            or stone_y >= self.height
        ):
            raise ValueError(f"Out of bounds: ({stone_x}, {stone_y})")
        self.stones[stone_y][stone_x] = value


class Game:
    """Game representation"""

    def __init__(self):
        """Constructor"""
        self.board = Board(20, 20)

    def new_board(self, length: int, height: int):
        """Creates a new empty board with the given length and height

        Args:
            length (int): Length of the board to create
            height (int): Height of the board to create
        """
        self.board = Board(length, height)

    def load_board(self, lines: list):
        """Loads a new board from a list of lines.

        Args:
            lines (list): Lines of the given format : x,y,value
        """
        self.board.load(lines)

    def new_turn(self, player: int, turn_x: int, turn_y: int):
        """Plays a new turn on the board.

        Args:
            player (int): _description_
            turn_x (_type_): _description_
            turn_y (_type_): _description_
        """
        self.board.add_stone(player, turn_x, turn_y)
