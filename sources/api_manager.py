from sys import stdin
from enum import Enum

ApiCommands = Enum(
    "ApiCommands", ["START", "TURN", "BEGIN", "BOARD", "INFO", "END", "ABOUT"]
)
BrainCommands = Enum(
    "BrainCommands", ["UNKNOWN", "ERROR", "MESSAGE", "DEBUG", "SUGGEST"]
)


class ApiManager:
    def __init__(self):
        self.__shutdown = False

    def shutting_down(self):
        return self.__shutdown

    @staticmethod
    def receive() -> str:
        line = stdin.readline()
        if not line:
            return "END"
        if line.endswith("\n"):
            line = line[:-1]
        return line

    @staticmethod
    def send(cmd: BrainCommands, message: str):
        if cmd not in list(BrainCommands):
            print('DEBUG Invalid brain command: "%s"' % cmd, flush=True)
            return
        message = "%s %s" % (cmd.name, message)
        print(message, flush=True)

    @staticmethod
    def answer(message: str):
        print(message, flush=True)
