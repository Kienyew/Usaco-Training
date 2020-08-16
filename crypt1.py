"""
ID: aobi1001
LANG: PYTHON3
TASK: crypt1
"""

from pathlib import Path

inputs = Path('crypt1.in').read_text().splitlines()
digits = [*map(int, inputs[1].split(' '))]


def combs():
    yield from ((a, b, c, d, e) for a in digits for b in digits for c in digits for d in digits for e in digits)


n = 0
for a, b, c, d, e in combs():
    abc = a * 100 + b * 10 + c

    partial_prod_1 = e * abc
    if len(str(partial_prod_1)) != 3:
        continue

    if any(int(digit) not in digits for digit in str(partial_prod_1)):
        continue

    partial_prod_2 = d * 10 * abc
    if len(str(partial_prod_2)) != 4:
        continue

    if any(int(digit) not in digits for digit in str(partial_prod_2)[:-1]):
        continue

    total = partial_prod_1 + partial_prod_2
    total_str = str(total)
    if len(total_str) != 4:
        continue

    if any(int(digit) not in digits for digit in total_str[:-1]):
        continue

    n += 1


with Path('crypt1.out').open('w') as fout:
    print(n, file=fout)
