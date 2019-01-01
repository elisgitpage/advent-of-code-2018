"""
Day 4 Advent of Code
https://adventofcode.com/2018/day/4

"""

import re
import datetime
from collections import defaultdict

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
guard_naps = []
for log in logs:
    #print(log)
    if log[1][0] is 'G':
        this_id = int(re.search(r'(\d+)', log[1]).group(0))
    if log[1][0] is 'f':
        this_start = log[0].minute
    if log[1][0] is 'w':
        this_finish = log[0].minute
    if this_id is not None and this_start is not None and this_finish is not None:
        this_nap = (this_id, this_start, this_finish)
        guard_naps.append(this_nap)
        this_start, this_finish = None, None

guards = defaultdict(list)
for nap in guard_naps:
    guards[nap[0]].append((nap[1], nap[2]))


def total_sleep(guard_naps):
    """

    :param guard_naps:
    :return:
    """
    tot = 0
    for nap in guard_naps:
        tot += nap[1] - nap[0]
    return tot


print(guard_naps[0])


def most_slept_min(guard_naps):
    """
    :param guard_naps: list of tuples representing start and finish times of naps of particular guards
    :return: max_min: integer representing minute in first hour of day spent asleep in highest number of naps
    """
    slept, max_min, max_slept = 0, 0, 0
    for m in range(60):
        slept = 0
        for nap in guard_naps:
            #print("minute {}, nap {}".format(m, nap))
            if nap[0] <= m and m < nap[1]:
                slept += 1
                #print('Was asleep!')
        if slept > max_slept:
            #print('slept: {}, minute: {}'.format(slept, m))
            max_min = m
            max_slept = slept
    return max_min, max_slept


sleepiest = 0
nap_max = 0
this_total = 0
for key, val in guards.items():
    #print(key, "=>",val)
    this_total = total_sleep(val)
    if this_total > nap_max:
        nap_max = this_total
        sleepiest = key

sleepiest_min = most_slept_min(guards.get(sleepiest))[0]
print("sleepiest guard id: {}, time slept: {}, sleepiest min: {}".format(sleepiest, nap_max, sleepiest_min))
print(sleepiest * sleepiest_min)

# PART 2
sleepiest, most_freq_min, this_freq, this_min, max_freq = 0, 0, 0, 0, 0
for key, val in guards.items():
    this_min, this_freq = most_slept_min(val)
    print("guard_id: {}, this_min:{}, this_freq:{}".format(key, this_min, this_freq))
    if this_freq > max_freq:
        max_freq = this_freq
        sleepiest = key
        most_freq_min = this_min

print("""guard most freq asleep same min: {},
         minute slept freq.: {},
         minute {}""".format(sleepiest, max_freq, most_freq_min))
print(sleepiest * most_freq_min)