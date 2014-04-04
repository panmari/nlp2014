

import re

# first group is non consuming
p = re.compile('(?=[^bB]).*[0-9]{2}.*')

with open('input_ex3.txt') as f:
    for line in f:
        if p.match(line):
            print(line.strip())