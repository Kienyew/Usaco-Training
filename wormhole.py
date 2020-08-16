"""
ID: aobi1001
LANG: PYTHON3
TASK: wormhole
"""

from pathlib import Path
from typing import Tuple, List, Iterator

Coord = Tuple[int, int]


fin = Path('wormhole.in')
fout = Path('wormhole.out')

inputs = fin.read_text().splitlines()
N = int(inputs[0])
coords = [(int(x), int(y)) for x, y in map(str.split, inputs[1:])]
right_of = {}

# Build a dict where right_of[coord] == first wormhole to the right from coord
for a in coords:
    rights = []
    for b in coords:
        if a == b:
            continue

        if a[1] != b[1]:
            continue

        if a[0] > b[0]:
            continue

        rights.append(b)

    if len(rights) != 0:
        next_right = min(rights, key=lambda coord: coord[0])
        right_of[a] = next_right


# create all pairs combinations
def all_pairs(options) -> Iterator[List[Tuple[Coord, Coord]]]:
    def backtrack(path: List[Coord], options: List[Coord]):
        if len(options) == 0:
            yield path.copy()
            return

        a = options.pop()
        for i in range(len(options)):
            b = options.pop(i)
            path.append((a, b))
            yield from backtrack(path, options)
            path.pop()
            options.insert(i, b)

        options.append(a)

    return backtrack([], options)


def pair_will_loop(pairs: List[Coord]) -> bool:
    paths = {}
    for a, b in pairs:
        paths[a] = b
        paths[b] = a

    for start in coords:
        position = start
        passed_positions = {start}
        while True:
            right = right_of.get(position)
            if right is None:
                break

            position = paths[right]
            if position in passed_positions:
                return True
            else:
                passed_positions.add(position)

    return False


n = 0
for pairs in all_pairs(coords[:]):
    if pair_will_loop(pairs):
        n += 1

with fout.open('w') as fout:
    print(n, file=fout)
