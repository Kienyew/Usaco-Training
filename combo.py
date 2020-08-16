"""
ID: aobi1001
LANG: PYTHON3
TASK: combo
"""

from pathlib import Path
from itertools import product
from typing import Tuple, Iterator

fin = Path('combo.in')
fout = Path('combo.out')
inputs = fin.read_text().splitlines()

N = int(inputs[0])
key_a = [*map(int, inputs[1].split(' '))]
key_b = [*map(int, inputs[2].split(' '))]
deltas = list(product((-2, -1, 0, 1, 2), repeat=3))

KeyType = Tuple[int, int, int]


def translated(key) -> Iterator[KeyType]:
    for dx, dy, dz in deltas:
        x = (key[0] + dx) % N
        y = (key[1] + dy) % N
        z = (key[2] + dz) % N
        yield (x, y, z)


n = len(set(translated(key_a)).union(translated(key_b)))
with fout.open('w') as fout:
    print(n, file=fout)
