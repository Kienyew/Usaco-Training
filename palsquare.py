"""
ID: aobi1001
LANG: PYTHON3
TASK: palsquare
"""

from pathlib import Path

base = int(Path('palsquare.in').read_text().strip())
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


with Path('palsquare.out').open('w') as fout:
    for i in range(1, 301):
        square = i ** 2
        square_base_str = base_str(square, base)
        if is_palindrome(square_base_str):
            fout.write(f'{base_str(i, base)} {square_base_str}\n')
