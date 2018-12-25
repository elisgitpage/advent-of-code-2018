import re
input_data = open('input_2.txt')
input_lines = input_data.read().splitlines()

match_2 = re.compile(r'^\w*?(\w)[^\1]*\1[^\1]*$')
counter2 = 0
match_3 = re.compile(r'^\w*?(\w)[^\1]*\1[^\1]*\1[^\1]*$')
counter3 = 0
for line in input_lines:
    thisMatch2 = match_2.match(line)

    if thisMatch2 is not None:
        counter2 += 1

for line in input_lines:
    thisMatch3 = match_3.match(line)

    if thisMatch3 is not None:
        counter3 += 1

print('input_lines counter:' + str(input_lines.__len__()))
print('counter3: ' + str(counter3))
print('counter2: ' + str(counter2))
print('checksum23: ' + str(counter2 * counter3))