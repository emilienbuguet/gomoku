"""Here is where the commands of the protocol are implemented"""

from .api_manager import ApiManager, ApiCommands, BrainCommands
from .game import Game, ME, ENEMY
from .brain import get_best_move


class Core:
    """The command handler, which creates a relation between the game and the API"""

    def __init__(self):
        self._game: Game = Game()
        self.__manager__: ApiManager = ApiManager()
        self.__shutdown__: bool = False
        self.__name__: str = "Gomorvin"
        self.__version__: str = "0.1"
        self.__author__: str = "Les Bebz"
        self.__country__: str = "France"

    def __handle_about__(self) -> str:
        return f'name="{self.__name__}", version="{self.__version__}", author="{self.__author__}", \
            country="{self.__country__}"'

    def __handle_start__(self, params: list) -> str:
        try:
            if len(params) == 2:
                self._game.new_board(params[0], params[1])
            else:
                self._game.new_board(params[0], params[0])
            if params[0] == "0":
                return "ERROR"
            return "OK"
        except ValueError:
            self.__manager__.send(BrainCommands.ERROR, "invalid parameters for START")
            return ""

    def __handle_board__(self) -> str:
        lines: list = []
        while 1:
            line = self.__manager__.receive()
            if line == "DONE":
                break
            lines.append(line)
        self._game.load_board(lines)
        turn_x, turn_y = get_best_move(self._game)
        self._game.new_turn(ME, turn_x, turn_y)
        return f"{turn_x},{turn_y}"

    def __handle_begin__(self) -> str:
        turn_x, turn_y = get_best_move(self._game)
        self._game.new_turn(ME, turn_x, turn_y)
        return f"{turn_x},{turn_y}"

    def __handle_turn__(self, params: list) -> str:
        try:
            turn_x = int(params[0])
            turn_y = int(params[1])
            self._game.new_turn(ENEMY, turn_x, turn_y)
        except (ValueError, IndexError):
            self.__manager__.send(BrainCommands.ERROR, "invalid parameters for TURN")
            return ""
        turn_x, turn_y = get_best_move(self._game)
        self._game.new_turn(ME, turn_x, turn_y)
        return f"{turn_x},{turn_y}"

    @staticmethod
    def __handle_info__() -> str:
        return ""

    def __handle_end__(self) -> str:
        self.__shutdown__ = True
        return ""

    def __handle__(self, cmd: ApiCommands, params: list) -> str:
        if cmd == ApiCommands.ABOUT:
            return self.__handle_about__()
        if cmd == ApiCommands.START:
            return self.__handle_start__(params)
        if cmd == ApiCommands.BOARD:
            return self.__handle_board__()
        if cmd == ApiCommands.BEGIN:
            return self.__handle_begin__()
        if cmd == ApiCommands.TURN:
            return self.__handle_turn__(params)
        if cmd == ApiCommands.INFO:
            return self.__handle_info__()
        if cmd == ApiCommands.END:
            return self.__handle_end__()
        return ""

    def start(self):
        """Starts the Core of the program."""
        while not self.__shutdown__:
            line: str = self.__manager__.receive()
            cmd: str = line.split(" ")[0]
            params: list = "".join(line.split(" ")[1:]).split(",")

            if cmd not in [c.name for c in list(ApiCommands)]:
                self.__manager__.send(
                    BrainCommands.UNKNOWN,
                    message=f'api command "{cmd}" is not supported.',
                )
                continue

            res: str = self.__handle__(cmd=ApiCommands[cmd], params=params)
            if res:
                self.__manager__.answer(res)
