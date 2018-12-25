'''
Day 3 advent of code puzzle
https://adventofcode.com/2018/day/3
'''

import re
input_data = open('input_3.txt')
input_lines = input_data.read().splitlines()

# regex to extract cloth patch data from input file lines
patch_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

# loop to fill 'patches' list with tuples of patch data
patches = []
for line in input_lines:
    # print(line)
    this_match = patch_regex.match(line)
    this_group = this_match.groups()
    a, b, c, d, e = this_group
    patch = [int(a), int(b), int(c), int(d), int(e)]
    patches.append(patch)
    # print(nums[0])

# loops to check each square inch for number of overlaps

# create 1000 by 1000 array of empty overlap counts
w, h = 1000, 1000;
material = [[0 for x in range(w)] for y in range(h)]

for patch in patches:
    idp, x, y, w, h = patch
    for i in range(x, x + w):
        for j in range(y, y + h):
            material[i][j] += 1

over2count = 0
found = False
idf = None
for row in material:
    for squinch in row:
        if squinch >= 2:
            over2count += 1

for patch in patches:
    def inner():
        global idf
        idp, x, y, w, h = patch
        for i in range(x, x + w):
            for j in range(y, y + h):
                if material[i][j] != 1:
                    return
        idf = idp

    inner()

print('id : ' + str(idf))
#print('x : ' + str(xf))
#print('y : ' + str(yf))

print(over2count)
'''
overlaps = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        this_overlap = 0
        # check each patch for overlap of current square inch
        for patch in patches:
            idp, x, y, w, h = patch
            if x <= i < x + w and y <= j < y + h:
                this_overlap += 1
                if this_overlap == 2:
                    overlaps += 1
                    continue
print(overlaps)
'''

"""
- sort patches into four lists
"""

