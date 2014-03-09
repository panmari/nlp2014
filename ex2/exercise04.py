

import re

# first and last name can be only capital letter
p = re.compile('[A-Z][^0-9]*\.[A-Z][^0-9]*@.+\.com')

with open('input_ex4.txt') as f:
    for line in f:
        if p.match(line):
            print(line.strip())