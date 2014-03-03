#!/usr/bin/python3


swiss_pages = []
with open('input_ex5.txt', 'r') as f:
    for line in f:
        if line.strip()[-3:] == '.ch':
            swiss_pages.append(line.strip())

print(swiss_pages)