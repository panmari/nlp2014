import re


def get_four_letter_words():
    four_letter_words = set()
    with open('input_ex1.txt') as f:
        for line in f.readlines():
            words = re.findall('[ ^]([a-zA-Z]{4})[.,: \n]', line)
            for word in words:
                four_letter_words.add(word.strip())
    return four_letter_words


# only print/write words if this script was called directly
if __name__ == '__main__':
    flw = get_four_letter_words()
    print('Found {} different four letter words:'.format(len(flw)))
    print(flw)
    print('Dumping to file...')
    with open('output_ex2.txt', 'w') as f:
        for word in flw:
            f.write(word + "\n")