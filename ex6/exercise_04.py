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