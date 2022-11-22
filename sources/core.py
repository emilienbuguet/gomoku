from api_manager import ApiManager, ApiCommands, BrainCommands
from game import Game, Players
import brain


class Core:

    def __init__(self):
        self.__game__: Game = Game()
        self.__manager__: ApiManager = ApiManager()
        self.__shutdown__: bool = False
        self.__name__: str = "Gomorvin"
        self.__version__: str = "0.1"
        self.__author__: str = "Les Bebz"
        self.__country__: str = "France"

    def __handle_about__(self) -> str:
        return 'name="%s", version="%s", author="%s", country="%s"' % (
            self.__name__, self.__version__, self.__author__, self.__country__)

    def __handle_start__(self, params: list) -> str:
        try:
            if len(params) == 2:
                self.__game__.new_board(params[0], params[1])
            else:
                self.__game__.new_board(params[0], params[0])
            if params[0] == "0":
                return "ERROR"
            return 'OK'
        except ValueError:
            self.__manager__.send(BrainCommands.ERROR, "invalid parameters for START")
            return None

    def __handle_board__(self) -> str:
        lines: list = list()
        while 1:
            line = self.__manager__.receive()
            if line == 'DONE':
                break
            lines.append(line)
        self.__game__.load_board(lines)
        x, y = brain.evaluate(self.__game__)
        self.__game__.new_turn(Players['ME'], x, y)
        return '%d,%d' % (x, y)

    def __handle_begin__(self) -> str:
        x, y = brain.evaluate(self.__game__)
        self.__game__.new_turn(Players['ME'], x, y)
        return "%d,%d" % (x, y)

    def __handle_turn__(self, params: list) -> str:
        try:
            x = int(params[0])
            y = int(params[1])
            self.__game__.new_turn(Players['ENNEMY'], x, y)
        except (ValueError, IndexError):
            self.__manager__.send(BrainCommands.ERROR, 'invalid parameters for TURN')
            return None
        x, y = brain.evaluate(self.__game__)
        self.__game__.new_turn(Players.ME, x, y)
        return '%d,%d' % (x, y)

    @staticmethod
    def __handle_info__(params: list) -> str:
        return None

    def __handle_end__(self) -> str:
        self.__shutdown__ = True
        return None

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
            return self.__handle_info__(params)
        if cmd == ApiCommands.END:
            return self.__handle_end__()
        return None

    def start(self):
        while not self.__shutdown__:
            line: str = self.__manager__.receive()
            cmd: str = line.split(' ')[0]
            params: list = ''.join(line.split(' ')[1:]).split(',')

            if cmd not in [c.name for c in list(ApiCommands)]:
                self.__manager__.send(BrainCommands.UNKNOWN, message='api command "%s" is not supported.' % cmd)
                continue

            res: str = self.__handle__(cmd=ApiCommands[cmd], params=params)
            if res is not None:
                self.__manager__.answer(res)
