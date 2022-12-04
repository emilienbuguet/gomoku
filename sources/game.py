"""Here is the gomoku implementation without GUI"""

ME = '1'
ENEMY = '2'


class Board:
    """This is the state of the current running gomoku game"""

    def __init__(self, length: int, height: int):
        self.length = int(length)
        self.height = int(height)
        self.stones_rows = [
            '0' * self.length for _ in range(0, self.height)
        ]
        self.stones_cols = [
            '0' * self.height for _ in range(0, self.length)
        ]
        self.left_diags = [
            '0' * size for size in range(1, self.height + 1)
        ]
        self.left_diags += self.left_diags[-2::-1]
        self.right_diags = [
            '0' * size for size in range(1, self.height + 1)
        ]
        self.right_diags += self.right_diags[-2::-1]

    def __str__(self) -> str:
        result: str = ""
        for i in range(0, self.height):
            result += "MESSAGE "
            for j in range(0, self.length):
                result += (
                    "_"
                    if self.stones_rows[i][j] == "0"
                    else "1"
                    if self.stones_rows[i][j] == "1"
                    else "2"
                )
                result += " "
            result += "\n" if i < self.height - 1 else ""
        return result

    def __getitem__(self, i: int) -> str:
        return self.stones_rows[i]

    def __setitem__(self, key, value):
        self.stones_rows[key] = value

    def load(self, lines: list):
        """Loads a new board from a list of lines.

        Args:
            lines (list): Lines of the given format : x,y,value
        """
        for line in lines:
            [x_coordinate, y_coordinate, value] = line.split(",")
            x_coordinate = int(x_coordinate)
            y_coordinate = int(y_coordinate)
            list_line = list(self.stones_rows[y_coordinate])
            list_line[x_coordinate] = value

            self.stones_rows[y_coordinate] = ''.join(list_line)

            col_list = list(self.stones_cols[x_coordinate])
            col_list[y_coordinate] = value

            self.stones_cols[x_coordinate] = ''.join(col_list)

            left_list = list(self.left_diags[x_coordinate + y_coordinate])
            if x_coordinate + y_coordinate <= self.length // 2:
                left_list[x_coordinate] = value
            else:
                left_list[x_coordinate - (self.length - len(left_list))] = value
            self.left_diags[x_coordinate + y_coordinate] = ''.join(left_list)

            right_list = list(self.right_diags[self.height - 1 - x_coordinate + y_coordinate])
            if x_coordinate < y_coordinate:
                right_list[x_coordinate] = value
            else:
                right_list[y_coordinate] = value
            self.right_diags[self.height - 1 - x_coordinate + y_coordinate] = ''.join(right_list)

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
        line_list = list(self.stones_rows[stone_y])
        line_list[stone_x] = value
        self.stones_rows[stone_y] = ''.join(line_list)

        col_list = list(self.stones_cols[stone_x])
        col_list[stone_y] = value
        self.stones_cols[stone_x] = ''.join(col_list)

        left_list = list(self.left_diags[stone_x + stone_y])
        if stone_x + stone_y <= self.length // 2:
            left_list[stone_x] = value
        else:
            left_list[stone_x - (self.length - len(left_list))] = value
        self.left_diags[stone_x + stone_y] = ''.join(left_list)

        right_list = list(self.right_diags[self.height - 1 - stone_x + stone_y])
        if stone_x < stone_y:
            right_list[stone_x] = value
        else:
            right_list[stone_y] = value
        self.right_diags[self.height - 1 - stone_x + stone_y] = ''.join(right_list)


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
