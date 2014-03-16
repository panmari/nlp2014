
import re
import collections

# this implementation tries to use fast data structures and prevents copying lists at all cost.

with open('input_ex4.txt') as f:
    # split() method splits on any whitespace by default
    arry = f.read().split()
    # turn arry into iterator with following filter
    arry = filter(lambda x: not re.match(r'[<>\d]+', x), arry)
    # TODO: possibly apply another filter or do splitting better to have
    # [..., "end", ".", ...]
    # instead of
    # [..., "end.", ...]

bigram_counter = collections.Counter()
before = next(arry)
for i in arry:
    bigram_counter[(before, i)] += 1
    before = i

print(bigram_counter.most_common(10))