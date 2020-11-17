"""


@author: Yauheni
"""

import tools


class View:
    def __init__(self) -> None:
        pass

    def print(self, message: str):
        print(f'view: {message} at: {tools.get_time()}')
