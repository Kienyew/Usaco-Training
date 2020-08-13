"""
ID: aobi1001
LANG: PYTHON3
TASK: gift1
"""

from pathlib import Path
from collections import deque

inputs = deque(Path('gift1.in').read_text().splitlines())
NP = int(inputs.popleft())
names = []
moneys = {}

for i in range(NP):
    name = inputs.popleft()
    names.append(name)
    moneys[name] = 0

while len(inputs) > 0:
    name = inputs.popleft()
    money_giveout, give_count = map(int, inputs.popleft().split(' '))
    if give_count != 0:
        money_per_giveout, money_left = divmod(money_giveout, give_count)
    else:
        money_per_giveout, money_left = 0, money_giveout

    moneys[name] += money_left - money_giveout
    for _ in range(give_count):
        recipient = inputs.popleft()
        moneys[recipient] += money_per_giveout

with Path('gift1.out').open('w') as fout:
    for name in names:
        print(f'{name} {moneys[name]}', file=fout)
