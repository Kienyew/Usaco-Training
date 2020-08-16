"""
ID: aobi1001
LANG: PYTHON3
TASK: transform
"""

from pathlib import Path
import copy

inputs = Path('transform.in').read_text().splitlines()
N = int(inputs[0])

ori_matrix = []
for i in range(N):
    row = list(inputs[1 + i])
    ori_matrix.append(row)

res_matrix = []
for i in range(N):
    row = list(inputs[N + 1 + i])
    res_matrix.append(row)


def rot90(matrix):
    N = len(matrix)
    res_matrix = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(N):
            res_matrix[i][j] = matrix[N - j - 1][i]

    return res_matrix


def reflect_horizontal(matrix):
    res_matrix = copy.deepcopy(matrix)
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            res_matrix[i][j] = matrix[i][N - j - 1]

    return res_matrix


def determine_transform(ori_matrix, res_matrix) -> int:
    rot90_matrix = rot90(ori_matrix)
    if rot90_matrix == res_matrix:
        return 1

    rot180_matrix = rot90(rot90_matrix)
    if rot180_matrix == res_matrix:
        return 2

    rot270_matrix = rot90(rot180_matrix)
    if rot270_matrix == res_matrix:
        return 3

    reflect_matrix = reflect_horizontal(ori_matrix)
    if reflect_matrix == res_matrix:
        return 4

    rr90_matrix = rot90(reflect_matrix)
    if rr90_matrix == res_matrix:
        return 5

    rr180_matrix = rot90(rr90_matrix)
    if rr180_matrix == res_matrix:
        return 5

    rr270_matrix = rot90(rr180_matrix)
    if rr270_matrix == res_matrix:
        return 5

    if ori_matrix == res_matrix:
        return 6

    return 7


transform = determine_transform(ori_matrix, res_matrix)
Path('transform.out').write_text(f'{transform}\n')
