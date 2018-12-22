''''
Day 1 advent of code puzzle
https://adventofcode.com/2018/day/1

'''
# TODO: Open input file
input = open('input.txt')

# dump file into list of strings
input_lines = input.read().splitlines()
# could also use readlines() but this would append \n to each line

# TODO: Loop through lines in file and track and print freq changes
counter = 0
freq_change = 0
for word in input_lines:
    freq_change = int(word)
    print('Current frequency {0}, change of {1}; resulting frequency'.format(counter, freq_change), end = " ")
    counter += freq_change
    print(" " + str(counter))

# TODO: print final freq.