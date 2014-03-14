

s = "Keep it short and simple!"

def make_n_grams(n, s):
    rangeCount = max(len(s) - n + 1, 0)
    # use list comprehensive to assemble list of ngrams (represented as tuples)
    return [tuple(s[i:i+n]) for i in range(rangeCount)]

three_grams = make_n_grams(3, s)

# could be printed directly, or as on assignment:
for gram in three_grams:
    print("{} {} {}".format(gram[0], gram[1], gram[2]))

# Or as in forum post
for gram in three_grams:
    s = ""
    for l in gram:
        if l == " ":
            s += "_"
        else:
            s += l
        s += " "
    print(s)