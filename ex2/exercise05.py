

import re

# additionally ignoring punctuation when checking word length
# the first group is non consuming, so it counts towards word length (and non-digit check)
p = re.compile('(?=[^A-Z])[^0-9,\.]{5,}')

with open('input_ex5.txt') as f:
    for line in f:
        # skip empty lines
        if line.strip() == '':
            continue
        word_count = 0
        for candidate_word in line.split():
            m = p.match(candidate_word)
            if m:
                if ':' in m.groups(0):
                    raise Exception('Contains colon')
                word_count += 1
        print("{}: {}".format(word_count, line.strip()))