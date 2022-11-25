"""Here are all the utilities for communicating with the Piskvork API, using its protocol"""

from sys import stdin
from enum import Enum, auto


class ApiCommands(Enum):
    """Enum of all the commands that can be sent by the Piskvork API"""
    START = auto()
    TURN = auto()
    BEGIN = auto()
    BOARD = auto()
    INFO = auto()
    END = auto()
    ABOUT = auto()


class BrainCommands(Enum):
    """Enum of all the commands that can be sent by the brain"""
    UNKNOWN = auto()
    ERROR = auto()
    MESSAGE = auto()
    DEBUG = auto()
    SUGGEST = auto()


class ApiManager:
    """Utility class for communicating with the API"""
    def __init__(self):
        self.__shutdown = False

    def shutting_down(self) -> bool:
        """Tells if the manager has to shut down

        Returns:
            bool: True if the manager has to shut down, False otherwise
        """
        return self.__shutdown

    @staticmethod
    def receive() -> str:
        """Gets the next command from the API

        Returns:
            str: The command received
        """
        line = stdin.readline()
        if not line:
            return "END"
        if line.endswith("\n"):
            line = line[:-1]
        return line

    @staticmethod
    def send(cmd: BrainCommands, message: str):
        """Sends a command to the Piskvork API

        Args:
            cmd (BrainCommands): The command to send
            message (str): The message to send
        """
        if cmd not in list(BrainCommands):
            print(f'DEBUG Invalid brain command: "{cmd}"', flush=True)
            return
        message = f"{cmd.name} {message}" % (cmd.name, message)
        print(message, flush=True)

    @staticmethod
    def answer(message: str):
        """Sends a message to the Piskvork API, without a command

        Args:
            message (str): The message to send"""
        print(message, flush=True)
