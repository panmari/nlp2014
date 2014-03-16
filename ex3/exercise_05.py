
import re

def give_contexts(search_term, n):
    with open('input_ex4.txt') as f:
        # split() method splits on any whitespace by default
        arry = f.read().split()
        arry = list(filter(lambda x: not re.match(r'[<>\d]+', x), arry))

    contexts = []
    for idx, word in enumerate(arry):
        if re.match(search_term, word):
            n_context = arry[idx-n:idx+n+1]
            start_context = 0
            end_context = 2*n + 1
            for idx, word in enumerate(n_context):
                # words that contain dots and are all uppercase are considered abbreviations (fixes "Charles VII.")
                if '.' in word and not word.isupper():
                    if idx < n:
                        start_context = idx + 1
                    else:
                        end_context = idx + 1
                        # break loop, bc there might be further dots ahead we want to ignore
                        break
            cropped_context = n_context[start_context:end_context]
            contexts.append((n_context, cropped_context))


    return contexts

print("\n".join([" ".join(y) for (x,y) in give_contexts('France', 5)]))
