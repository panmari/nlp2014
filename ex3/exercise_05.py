
import re
import sys


def give_contexts(search_term, n):
    with open('input_ex4.txt') as f:
        # split() method splits on any whitespace by default
        arry = f.read().split()
        arry = list(filter(lambda x: not re.match(r'[<>\d]+', x), arry))

    contexts = []
    for idx, word in enumerate(arry):
        if re.match(search_term, word, re.IGNORECASE):
            n_context = arry[idx-n:idx+n+1]
            start_context = 0
            end_context = len(n_context)
            for idx, word in enumerate(n_context):
                # words that contain dots and are all uppercase are considered abbreviations (fixes "Charles VII.")
                # if ',' and '.' appear both in one word, the point was for an abbreviation!
                if '.' in word and not word.isupper() and not ',' in word:
                    if idx < n:
                        start_context = idx + 1
                    else:
                        end_context = idx + 1
                        # break loop, bc there might be further dots ahead we want to ignore
                        break
            cropped_context = n_context[start_context:end_context]
            contexts.append((n_context, cropped_context))


    return contexts

# read out command line argument
try:
    context_size = int(sys.argv[1])
except:
    context_size = 10
    print("No argument given, using default of {} as context size".format(context_size))

contexts = give_contexts('France', context_size)
print("Found {} matches:".format(len(contexts)))
print("\n".join([" ".join(y) for (x,y) in contexts]))
