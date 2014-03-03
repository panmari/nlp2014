

import re

p = re.compile('.*a.*a.*a.*')

with open('input_ex2.txt') as f:
    for line in f:
        if p.match(line):
            print(line.strip())