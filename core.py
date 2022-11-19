"""This is where the AI core class is implemented"""
from api_manager import ApiManager, ApiCommands, BrainCommands
from game import Game


class Core:
    """Core class of the AI"""
    def __init__(self):
        """Constructor"""
        self.__game__: Game | None = None
        self.__manager__: ApiManager = ApiManager()
        self.__shutdown__: bool = False

    def __handle__(self, cmd: ApiCommands, params: list) -> str:
        # Todo: Handle the ABOUT, START, END, BEGIN and TURN commands
        return "Executing %s with %s" % (str(cmd), str(params))

    def start(self):
        while not self.__shutdown__:
            line: str = self.__manager__.receive()
            cmd: str = line.split(' ')[0]
            params: list[str] = line.split(' ')[1:]

            if cmd not in [c.name for c in list(ApiCommands)]:
                self.__manager__.send(BrainCommands.UNKNOWN, message='api command "%s" is not supported.' % cmd)
                continue

            res: str = self.__handle__(cmd=ApiCommands[cmd], params=params)
            self.__manager__.send(BrainCommands.DEBUG, res)
