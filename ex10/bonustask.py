import re
from math import log2
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
            # do some sanitizing
            word = word.lower()
            word = word.strip("\"")
            word = word.strip(",")
            word = word.strip(".")
            word = word.strip(":")
            if word in most_frequent_words:
                profile[word] += 1
                size += 1
    return profile, size


def get_relative_frequency(profile, size):
    """
    returns the relative frequency of the profile, sorted by the terms lexicographically.
    """
    return [float(x[1])/size for x in sorted(profile.items())]

profile_a1, size_a1 = build_profile([2,3,4])
profile_a2, size_a2 = build_profile([15,16,17])

rf_a1 = get_relative_frequency(profile_a1, size_a1)
rf_a2 = get_relative_frequency(profile_a2, size_a2)

profile_q1, size_q1 = build_profile([37])
profile_q2, size_q2 = build_profile([8])

rf_q1 = get_relative_frequency(profile_q1, size_q1)
rf_q2 = get_relative_frequency(profile_q2, size_q2)


def compute_KLD(rf_profiles, rf_query):
    klds = [0] * len(rf_profiles)
    for idx, rf_profile in enumerate(rf_profiles):
        assert len(rf_profile) == len(rf_query)
        for aj, q in zip(rf_profile, rf_query):
            klds[idx] += q * log2(q/aj)
    return klds

klds_q1 = compute_KLD([rf_a1, rf_a2], rf_q1)
klds_q2 = compute_KLD([rf_a1, rf_a2], rf_q2)

print('For text nr 37 as query text:')
print(klds_q1)
print("Most likely none of these two is the author\n")

print('For text nr 8 as query text:')
print(klds_q2)
print("Author 1 could possibly be the author of this text.")
