"""
Class with some tools method, for example random int generator for ids
"""

import random
from datetime import datetime


def generate_random_int() -> int:
    return random.randint(1, 10000)


def get_time() -> str:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


class TransactionAccomplishedError(Exception):
    pass
