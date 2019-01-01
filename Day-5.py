'''
Day 5 advent of code puzzle

https://adventofcode.com/2018/day/5
'''

from string import ascii_lowercase

input_data = open('input_5.txt')  # open polymer list
pol = list(input_data.read().strip('\n'))  # read in list to string, strip \n and convert to list
exam_pol = list('dabAcCaCBAcCcaDA')
print(pol)


def reacting(pols: list, i: int):
    this_letter = pols[i]
    next_letter = pols[i + 1]
    return this_letter.lower() == next_letter.lower() and this_letter != next_letter


def react_polymers(pol):
    i = 0
    while i < pol.__len__() - 1:
        if reacting(pol, i):
            pol.pop(i)
            pol.pop(i)
            if i != 0:
                i -= 1
        else:
            i += 1
    return pol.__len__()


print(react_polymers(pol))
# PART 2

pols = list(open('input_5.txt').read().strip('\n'))


def filter_pol_type(listpol, unit):
    new = []
    for p in listpol:
        if p != unit and p != unit.upper():
            new.append(p)
    return new

this_len = 0
shortest_pol = pols.__len__()
opt_pol = ''
for c in ascii_lowercase:
    this_len = react_polymers(filter_pol_type(pols, c))
    if this_len < shortest_pol:
        shortest_pol = this_len
        opt_pol = c
print(f'{opt_pol:5}{shortest_pol}')

