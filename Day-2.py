'''
Day 2 advent of code puzzle
https://adventofcode.com/2018/day/2
'''



import re
from string import ascii_lowercase

input_data = open('input_2.txt')
input_lines = input_data.read().splitlines()
# print(input_lines)

count2 = 0
count3 = 0
for line in input_lines:
    line2 = False
    line3 = False
    for c in ascii_lowercase:
        if line.count(c) == 2:
            line2 = True
        if line.count(c) == 3:
            line3 = True
    if line2:
        count2 += 1
    if line3:
        count3 += 1

print('counter3: ' + str(count3))
print('counter2: ' + str(count2))
print('checksum23: ' + str(count2 * count3))
print('input_lines counter:' + str(input_lines.__len__()))


'''

match_2 = re.compile(r'^\w*?(\w)[^\1]*\1[^\1]*$')
counter2 = 0
match_3 = re.compile(r'^\w*?(\w)[^\1]*\1[^\1]*\1[^\1]*$')
counter3 = 0
for line in input_lines:
    thisMatch2 = match_2.match(line)

    if thisMatch2 is not None:
        # print(thisMatch2)
        # print('letter with 2 matches: ' + thisMatch2.group(1))
        counter2 += 1

for line in input_lines:
    thisMatch3 = match_3.match(line)

    if thisMatch3 is not None:
        print(thisMatch3)
        print('letter with 3 matches: ' + thisMatch3.group(1))
        counter3 += 1

print('counter3: ' + str(counter3))
print('counter2: ' + str(counter2))
print('checksum23: ' + str(counter2 * counter3))
print('input_lines counter:' + str(input_lines.__len__()))
'''

#TODO Part 2:

# TODO create function to check if 2 IDs are 1 character off


def one_off(a: str, b: str):
    common = ''
    off_count = 0
    for l in range(0, a.__len__()):
        if a[l] != b[l]:
            common = a[:l] + a[l+1:]
            off_count += 1

    if off_count == 1:
        return common
    else:
        return None


# For each ID, check remaining ID's if 1 character off
length = input_lines.__len__()
for i in range(0, length - 1):
    for j in range(i + 1, length):
        a, b = input_lines[i], input_lines[j]
        one_letter = one_off(a, b)
        if one_letter is not None:
            print()
            print(one_letter)
            print(a + '\n' + b)
