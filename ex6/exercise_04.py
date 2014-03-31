# do Soundex, compute levenstein distance on that (allow swapping of letters).

soundex_translator = { 1: ['B', 'F', 'P', 'V'],
                       2: ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'],
                       3: ['D', 'T'],
                       4: ['L'],
                       5: ['M', 'N'],
                       6: ['R']}

soundex_translator_inv = dict()
for number,letter_list in soundex_translator.items():
    for letter in letter_list:
        soundex_translator_inv[letter] = str(number)


input = 'teeeeesttt'
soundex_string = input[0]
for char in input[1:]:
    # get with empty string as default value
    soundex_append = soundex_translator_inv.get(char.upper(), '')
    if soundex_append != soundex_string[-1]:
        soundex_string += soundex_append

print(soundex_string)