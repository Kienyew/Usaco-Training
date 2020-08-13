"""
ID: aobi1001
LANG: PYTHON3
TASK: beads
"""

#            w w w b b r w r b r b r r b r b r w r w w r b w r w r r b
#
# acc_right: 5 4 3 2 1 3 2 1 1 1 1 2 1 1 1 1 6 5 4 3 2 1 2 5 4 3 2 1 6
# acc_left : 1 2 3 4 5 6 1 2 3 1 1 1 1 2 1 1 1 1 2 3 4 5 6 1 2 2 3 4 5

from pathlib import Path


def color_ok(c1, c2) -> bool:
    if c1 == 'w' or c2 == 'w':
        return True
    else:
        return c1 == c2


_, string = Path('beads.in').read_text().splitlines()

acc_right = [0] * len(string)
acc_left = [0] * len(string)

# acc right
for i in range(len(string)):
    original_i = i
    color = 'w'  # not yet determined color, default to white
    while True:
        if not color_ok(color, string[i]):
            break

        color = color if color != 'w' else string[i]
        acc_right[original_i] += 1
        i = (i + 1) % len(string)

        if i == original_i:
            break


# acc left
for i in range(len(string)):
    original_i = i
    color = 'w'  # not yet determined color, default to white
    i -= 1  # python handle string[-1] for us
    while True:
        if not color_ok(color, string[i]):
            break

        color = color if color != 'w' else string[i]
        acc_left[original_i] += 1
        i = (i - 1) % len(string)

        if i == original_i:
            break

result = max(r + l for r, l in zip(acc_right, acc_left))

# whole string only one color (doesnt count 'w')
if result > len(string):
    result = len(string)

with Path('beads.out').open('w') as fout:
    print(result, file=fout)
