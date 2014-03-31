import re

four_letter_words = set()

with open('input_ex1.txt') as f:
    for line in f.readlines():
        words = re.findall('[ ^]([a-zA-Z]{4})[., \n]', line)
        for word in words:
            four_letter_words.add(word.strip())

print('Found {} different four letter words:'.format(len(four_letter_words)))
print(four_letter_words)