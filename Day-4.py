"""
Day 4 Advent of Code
https://adventofcode.com/2018/day/4

"""

import re
import datetime
input_data = open('input_4.txt')
input_lines = input_data.read().splitlines()  # input guard logs text file as single string

# regex to extract time stamp data and text from guard logs text file
guard_regex = re.compile(r'\[1518-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (.*)')
# guard_regex = re.compile(r'\[(.*)\] (.*)')
logs = []
for line in input_lines:
    # print(line)
    this_match = guard_regex.match(line).groups()
    this_tuple = tuple(map(int, this_match[0:4]))
    # print(this_tuple)
    dt = datetime.datetime(1518, this_tuple[0], this_tuple[1], this_tuple[2], this_tuple[3])
    # print(dt)
    logs.append((dt, this_match[4]))

logs.sort(key=lambda l: l[0])
this_id = None
this_start = None
this_finish = None
this_nap = None
# guard_naps = [][]
for log in logs:
    print(log)
    if log[1][0] is 'G':
        this_id = int(re.search(r'(\d+)', log[1]).group(0))
    if log[1][0] is 'f':
        this_start = log[0].minute
    if log[1][0] is 'w':
        this_finish = log[0].minute
    if this_id is not None and this_start is not None and this_finish is not None:
        this_nap = (this_id, this_start, this_finish)
        print(this_nap)
