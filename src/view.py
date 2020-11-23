"""


@author: Yauheni
"""

from src.tools import get_time


class View:
    def __init__(self) -> None:
        pass

    def print(self, message: str):
        print(f'view: {message} at: {get_time()}')
