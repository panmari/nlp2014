# do Soundex, compute levenstein distance on that (allow swapping of letters).

class soundex:

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
            # get with empty string as default value
            soundex_append = self.soundex_translator_inv.get(char.upper(), '')
            if soundex_append != '0' and soundex_append != soundex_string[-1]:
                soundex_string += soundex_append
        if len(soundex_string) < 4:
            soundex_string += '0'*(4-len(soundex_string))
        return soundex_string

import numpy

class damerauLevenshtein:

    def compute(self, first, second):
        # d is a table with lenStr1+1 rows and lenStr2+1 columns
        d = numpy.zeros(len(first)*len(second)).reshape((len(first), len(second)))

        for i,c in enumerate(first):
            d[i, 0] = i
        for j,c in enumerate(second):
            d[0, j] = j

        # pseudo-code assumes string indices start at 1, not 0
        # if implemented, make sure to start comparing at 1st letter of strings
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
