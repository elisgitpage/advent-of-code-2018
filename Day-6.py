'''
Day 6 advent of code puzzle

https://adventofcode.com/2018/day/6
'''

import re

input_data = open('input_6.txt')
coord_lines = input_data.read().splitlines()
reg = re.compile(r'(\d+), (\d+)')
coords = []
for line in coord_lines:
    coords.append(tuple(map(int, reg.match(line).groups())))


def man_dist(c1, c2):
    '''

    :param c1:
    :param c2:
    :return: manhattan distance between coordinates p1 and p2
    '''
    return abs(c2[0] - c1[0]) + abs(c2[1] - c1[1])

x_max = 0
y_max = 0
for cord in coords:
    if cord[0] > x_max:
        x_max = cord[0]
    if cord[1] > y_max:
        y_max = cord[0]

coord_copy = coords.copy()
coord_copy.sort(key=lambda tup: tup[0])
coord_counter = 0
for y in range(1, y_max + 1):
    for x in range(1,x_max + 1):
        for i in range(0,coord_copy.__len__()):
            if coord_copy[i][0]==x and coord_copy[i][1]==y:
                print(f'{coord_counter} ', end='')
                coord_counter += 1
                break
            print('o', end='')
    print('')





#dist = man_dist(coords[0], coords[1])
#print(dist)


