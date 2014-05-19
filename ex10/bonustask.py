import re
with open('input_2.txt') as f:
    documents = {}
    doc_nr = None
    for line in f:
        doc_nr_match = re.match("<DOCNO>(\d+)</DOCNO>", line)
        if doc_nr_match:
            parsing = False
            doc_nr = int(doc_nr_match.groups(0)[0])
            documents[doc_nr] = ""
        if parsing:
            documents[doc_nr] += line
        if re.match('</SOURCE>', line):
            parsing = True

most_frequent_words = set()
with open('frequent100.txt') as f:
    for line in f:
        most_frequent_words.add(line.strip())


def build_profile(texts):
    profile = dict()
    # initialize with one for smoothing
    for word in most_frequent_words:
        profile[word] = 1
    size = 100 # initialized with 100 from smoothing
    # go over all words, add if it belongs to most frequent ones
    for t in texts:
        for word in re.split("\s", documents[t]):
            word = word.lower()
            if word in most_frequent_words:
                profile[word] += 1
                size += 1
    return profile, size

profile_a1, size_a1 = build_profile([2,3,4])
profile_a2, size_a2 = build_profile([15,16,17])
print(profile_a1)
print(profile_a2)