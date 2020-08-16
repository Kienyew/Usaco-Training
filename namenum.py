"""
ID: aobi1001
LANG: PYTHON3
TASK: namenum
"""

# import requests
from pathlib import Path

serial = Path('namenum.in').read_text().strip()
# ok_names = set(requests.get('https://train.usaco.org/usaco/namenumdict.txt').text.splitlines())
ok_names = set(Path('dict.txt').read_text().splitlines())

'''
ARGUMENTS
---------
path: current path, a string
digits: string of digits representing each number on number pad on the so called phone
ok_names: set of still possible name
'''

keypad = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PRS',
    '8': 'TUV',
    '9': 'WXY',
}


def track(path: str, digits: str, ok_names: set) -> list:
    if not any(name.startswith(path) for name in ok_names):
        return

    if len(digits) == 0:
        yield path
        return

    options = keypad[digits[0]]
    for option_char in options:
        new_path = path + option_char
        yield from track(new_path, digits[1:], ok_names)


names = filter(lambda name: name in ok_names, track('', serial, ok_names))
with Path('namenum.out').open('w') as fout:
    n = 0
    for name in names:
        n += 1
        fout.write(f'{name}\n')

    if n == 0:
        fout.write('NONE\n')
