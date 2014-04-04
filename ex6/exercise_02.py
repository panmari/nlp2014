from ex6.exercise_01 import get_four_letter_words
import string
import codecs
en_dictionary = set()

with codecs.open('english_dictionary.txt', encoding='iso-8859-15', mode='r') as f:
    for line in f.readlines():
        en_dictionary.add(line.strip())

flw = get_four_letter_words()

valid_constructed_flw = set()
for word in flw:
    for i in range(len(word)):
        # checks substitution with upper- as well as lowercase letter.
        for char in string.ascii_letters:
            word_changed = word[:i] + char + word[i+1:]
            if word_changed in en_dictionary:
                valid_constructed_flw.add(word_changed)

print(valid_constructed_flw)