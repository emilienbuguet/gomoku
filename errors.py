"""This is the file where all errors are declared"""


class Error(Exception):
    """Base error class"""
    pass


class UnknownCommandError(Error):
    """Error that is raised when a command is not handled"""
    pass


class BadCommandError(Error):
    """Error that is raised when a command has bad arguments"""
    pass
