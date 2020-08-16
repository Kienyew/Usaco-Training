"""
ID: aobi1001
LANG: PYTHON3
TASK: barn1
"""

from pathlib import Path
from collections import deque

inputs = deque(Path('barn1.in').read_text().splitlines())
M, S, C = inputs.popleft().split(' ')
M, S, C = int(M), int(S), int(C)

cows = set(int(inputs.popleft()) for _ in range(C))
blocks = [(min(cows), max(cows) + 1)]

ranges_no_cow = []
left = 0
right = 0
while right < S:
    right += 1
    if right in cows:
        if left != right:
            ranges_no_cow.append((left, right))
        left = right + 1

if S not in cows:
    ranges_no_cow.append((left, S))


# block range from shorter to longer from left to right
ranges_no_cow.sort(key=lambda x: x[1] - x[0])

while len(blocks) < M and len(ranges_no_cow) > 0:
    # max(right - left) where range(left, right) contains no cow
    left, right = ranges_no_cow.pop()

    for block in blocks:
        # range(left, right) is sub range of range(block[0], block[1])
        if left >= block[0] and right <= block[1]:
            break
    else:
        continue

    blocks.remove(block)
    if block[0] != left:
        blocks.append((block[0], left))

    if right != block[1]:
        blocks.append((right, block[1]))

stalls_blocked = sum(block[1] - block[0] for block in blocks)
with Path('barn1.out').open('w') as fout:
    print(stalls_blocked, file=fout)
