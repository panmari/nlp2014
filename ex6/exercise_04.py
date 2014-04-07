# do Soundex, compute levenstein distance on that (allow swapping of letters).

class Soundex:

    def __init__(self):
        soundex_translator = { 0: ['A', 'E', 'I', 'O', 'U', 'H', 'W', 'Y'],  # ignore these
                               1: ['B', 'F', 'P', 'V'],
                               2: ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'],
                               3: ['D', 'T'],
                               4: ['L'],
                               5: ['M', 'N'],
                               6: ['R']}

        self.soundex_translator_inv = dict()
        for number, letter_list in soundex_translator.items():
            for letter in letter_list:
                self.soundex_translator_inv[letter] = str(number)

    def encode(self, input):
        soundex_string = input[0]
        for char in input[1:]:
            # get with empty string as default value, so we can handle unknown characters
            soundex_append = self.soundex_translator_inv.get(char.upper(), '')
            if soundex_append != '0' and soundex_append != soundex_string[-1]:
                soundex_string += soundex_append
        if len(soundex_string) < 4:
            soundex_string += '0'*(4-len(soundex_string))
        return soundex_string

import numpy

class DamerauLevenshtein:

    def compute(self, first, second):
        # Using a numpy matrix for summing up distance
        d = numpy.zeros(len(first)*len(second)).reshape((len(first), len(second)))

        for i,c in enumerate(first):
            d[i, 0] = i
        for j,c in enumerate(second):
            d[0, j] = j

        for i, c_first in enumerate(first):
            for j, c_second in enumerate(second):
                if c_first == c_second:
                    cost = 0
                else:
                    cost = 1
                d[i, j] = min(d[i-1, j  ] + 1,     # deletion
                              d[i  , j-1] + 1,     # insertion
                              d[i-1, j-1] + cost)  # substitution
                if i > 1 and j > 1 and c_first == second[j-1] and first[i-1] == c_second:
                    d[i, j] = min(d[i, j],
                                  d[i-2, j-2] + cost)   # transposition

        return d[-1, -1]

from exercise_01 import get_four_letter_words

def spellcheck(word):
    flw = get_four_letter_words()
    s = Soundex()
    word_soundex = s.encode(word)
    possible_soundex_corrections = list()
    for w in flw:
        if word_soundex == s.encode(w):
            possible_soundex_corrections.append(w)
    d = DamerauLevenshtein()
    correction_distances = dict(zip(possible_soundex_corrections, [d.compute(x, word) for x in possible_soundex_corrections]))
    # sort dictionary by distances (converts to tuple for this purpose)
    sorted_corrections = sorted(correction_distances.items(), key=lambda x: x[1])
    print('Found the following possible correct spellings, ordered by distance:')
    for tuple in sorted_corrections:
        print(tuple)


import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        spellcheck(sys.argv[1])
    else:
        # run test:
        # gian -> misspelling for gain (does work)
        # rack -> misspelling for rock (does work)
        # deyn -> misspelling for deny (does work)
        # cas -> misspelling for case (does work)
        # gail -> misspelling for jail (does not work, since soundex gives too much weight to first character)
        for testword in ['gian', 'rack', 'deyn', 'cas', 'gail']:
            print("Doing spellcheck for {}...".format(testword))
            spellcheck(testword)
            print("\n")
