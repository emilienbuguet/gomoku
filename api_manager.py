"""This is the file where the class that communicates with the Piskvork api is implemented."""
from sys import stdin
from enum import Enum

ApiCommands = Enum('ApiCommands', ['START', 'TURN', 'BEGIN', 'BOARD', 'INFO', 'END', 'ABOUT'])
BrainCommands = Enum('BrainCommands', ['UNKNOWN', 'ERROR', 'MESSAGE', 'DEBUG', 'SUGGEST'])


class ApiManager:
    """This is the utility class to communicate with the Piskvork api."""

    def __init__(self):
        """Constructor."""
        self.__shutdown = False

    def shutting_down(self):
        """Check if the manager is shutting down."""
        return self.__shutdown

    @staticmethod
    def receive() -> str:
        """Get the next command from the api
        :return: The received command line
        """
        line = stdin.readline()
        if not line:
            return "END"
        if line.endswith('\n'):
            line = line[:-1]
        return line

    @staticmethod
    def send(cmd: BrainCommands, message: str):
        """Sends a command to the api"""
        if cmd not in list(BrainCommands):
            print('DEBUG Invalid brain command: "%s"' % cmd)
            return
        message = "%s %s" % (cmd.name, message)
        print(message, flush=True)

    @staticmethod
    def answer(message: str):
        """Answers to an api command"""
        print(message, flush=True)
