"""
ID: aobi1001
LANG: PYTHON3
TASK: friday
"""

from pathlib import Path


def is_leap(year: int) -> bool:
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


N = int(Path('friday.in').read_text().strip())

year = 1900
month = 0
day = 0
week_day = 1

days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_days_of_12 = [0, 0, 0, 0, 0, 0, 0]

while year < 1900 + N:
    if day == 12:
        week_days_of_12[week_day] += 1

    if day == days_of_month[month]:
        day = 0
        month += 1
        if month == 1 and is_leap(year):
            days_of_month[1] = 29
        else:
            days_of_month[1] = 28

    if month == 12:
        month = 0
        year += 1

    week_day = (week_day + 1) % 7
    day += 1

week_days_of_12 = [week_days_of_12[(6 + i) % 7] for i in range(7)]
with Path('friday.out').open('w') as fout:
    output = ' '.join(map(str, week_days_of_12))
    print(output, file=fout)
