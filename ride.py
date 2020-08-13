"""
ID: aobi1001
LANG: PYTHON3
TASK: ride
"""
from math import prod
from pathlib import Path


def I(c):
    return ord(c) - ord('A') + 1


a, b = Path('ride.in').read_text().splitlines()

mod_a = prod(map(I, a)) % 47
mod_b = prod(map(I, b)) % 47

Path('ride.out').write_text('GO\n' if mod_a == mod_b else 'STAY\n')
