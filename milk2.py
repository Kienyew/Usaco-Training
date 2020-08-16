"""
ID: aobi1001
LANG: PYTHON3
TASK: milk2
"""

from pathlib import Path

inputs = Path('milk2.in').read_text().splitlines()[1:]

time_points = []
for input_line in inputs:
    start, end = map(int, input_line.split(' '))
    time_points.append((start, +1))
    time_points.append((end, -1))

time_points.sort(key=lambda x: (x[0], -x[1]))
working_time = 0
idle_time = 0
max_working_time = 0
max_idle_time = 0
people_on_work = 0
last_time_point = time_points[0][0]

for i in range(len(time_points)):
    time_point, event = time_points[i]
    people_on_work += event

    if people_on_work == 0:
        working_time += time_point - last_time_point
        max_working_time = max(max_working_time, working_time)
        working_time = 0
    elif people_on_work == 1 and event == +1:
        idle_time += time_point - last_time_point
        max_idle_time = max(max_idle_time, idle_time)
        idle_time = 0
    else:
        working_time += time_point - last_time_point

    last_time_point = time_point

with Path('milk2.out').open('w') as fout:
    print(f'{max_working_time} {max_idle_time}', file=fout)
