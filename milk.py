"""
ID: aobi1001
LANG: PYTHON3
TASK: milk
"""

from pathlib import Path
from collections import deque

inputs = deque(Path('milk.in').read_text().splitlines())
N, M = inputs.popleft().split(' ')
N, M = int(N), int(M)

farms = []
for _ in range(M):
    P, A = inputs.popleft().split(' ')
    P, A = int(P), int(A)
    farms.append((P, A))

farms.sort(key=lambda farm: -farm[0])
milk = 0
cost = 0
while milk < N:
    P, A = farms.pop()
    unit = min(A, N - milk)
    milk += A
    cost += P * unit

with Path('milk.out').open('w') as fout:
    print(cost, file=fout)
