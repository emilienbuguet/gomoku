"""This is where the AI core class is implemented"""
from api_manager import ApiManager, ApiCommands, BrainCommands
from game import Game


class Core:
    """Core class of the AI"""
    def __init__(self):
        """Constructor"""
        self.game = None
        self.manager = ApiManager()

    def start(self):
        line: str = self.manager.receive()
        cmd: str = line.split(' ')[0]
        params: list[str] = line.split(' ')[1:]
        if cmd not in [c.name for c in list(ApiCommands)]:
            self.manager.send(BrainCommands.UNKNOWN, message='api command "%s" is not supported.' % cmd)
        # Handler.handle(cmd, params)
