"""
ID: aobi1001
LANG: PYTHON3
TASK: dualpal
"""

from pathlib import Path

N, S = Path('dualpal.in').read_text().strip().split()
N, S = int(N), int(S)

base_digits = '0123456789ABCDEFGHIJ'


def is_palindrome(s):
    return all(s[len(s) - i - 1] == s[i] for i in range(len(s) // 2))


def base_str(num: int, base: int) -> str:
    if num == 0:
        return '0'

    digits = []
    while num > 0:
        num, rem = divmod(num, base)
        digits.append(base_digits[rem])

    return ''.join(reversed(digits))


def ok(n: int) -> bool:
    count = 0
    for base in range(2, 11):
        if is_palindrome(base_str(n, base)):
            count += 1
            if count >= 2:
                return True

    return False


with Path('dualpal.out').open('w') as fout:
    count = 0
    for n in range(S + 1, 2**31 - 1):
        if ok(n):
            count += 1
            print(n, file=fout)
            if count >= N:
                break
