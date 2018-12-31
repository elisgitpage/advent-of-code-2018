'''
Day 5 advent of code puzzle

https://adventofcode.com/2018/day/5
'''

from string import ascii_lowercase

def reacting(pols: list, i: int):
    this_letter = pols[i]
    next_letter = pols[i + 1]
    return this_letter.lower() == next_letter.lower() and this_letter != next_letter


input_data = open('input_5.txt') # open polymer list
pol = list(input_data.read().strip('\n')) # read in list to string, strip \n and convert to list
#pol = list('dabAcCaCBAcCcaDA')
print(pol)


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


def filter_pols(listpol, unit):
    new = listpol.copy()
    new.remove(unit)
    new.remove(unit.upper())
    return new


print(['A'])
print(filter_pols(['A'], 'a'))
#for c in ascii_lowercase:
#    print(c + str(react_polymers(filter_pols(pols, c))))


