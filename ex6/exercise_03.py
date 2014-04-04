
from ex6.exercise_01 import get_four_letter_words
import string
import sys

def spellcheck(word):
    flw = get_four_letter_words()
    possible_correct_spellings = set()
    # case one: one letter in the word was missing
    for i in range(len(word)):
        for char in string.ascii_letters:
            word_changed = word[:i] + char + word[i+1:]
            if word_changed in flw:
                possible_correct_spellings.add(word_changed)

    # case two: two letters were swapped
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            word_changed = list(word)
            tmp = word_changed[i]
            word_changed[i] = word_changed[j]
            word_changed[j] = tmp
            word_changed = ''.join(word_changed)
            if word_changed in flw:
                possible_correct_spellings.add(word_changed)

    return possible_correct_spellings

sys.argv.append('eerh')
if len(sys.argv) != 2:
    print('Give exactly one word as parameter')
else:
    corrections = spellcheck(sys.argv[1])
    print('Found {} possible words:'.format(len(corrections)))
    print(corrections)