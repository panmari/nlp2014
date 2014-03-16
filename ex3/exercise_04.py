
import re
import collections
import sys
# this implementation tries to use fast data structures and prevents copying lists at all cost (would need lots of
# memory and is slow).

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

# read out command line argument
try:
    minimal_count = int(sys.argv[1])
except:
    minimal_count = 20
    print("No argument given, using default of {} as minimal threshold".format(minimal_count))

with open('output_ex4_bigrams.txt', 'w') as f:
    for bigram, count in bigram_counter.most_common(len(bigram_counter)):
        if count < minimal_count:
            break
        f.write("{} {}\n".format(bigram, count))
