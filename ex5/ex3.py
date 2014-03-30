
import re

from ex5.my_dictionary import MyDictionary

my_dict = MyDictionary(500)
with open('input_ex3.txt') as f:
    for line in f.readlines():
        words = re.findall('[a-zA-Z]{3,}[., \n]', line)
        for word in words:
            try:
                my_dict.insert(word.strip())
            except KeyError as e:
                pass #dont care

print("Size: {}".format(my_dict.size()))
print("Capacity: {}".format(my_dict.capacity))

collisions = 0
max_collision_count = 0
for list in my_dict.d:
    # only values above 1 are considered as collision
    if len(list) > 1:
        current_collision_count = len(list) - 1
        collisions += current_collision_count
        if (current_collision_count > max_collision_count):
            max_collision_count = current_collision_count

print("Max collision count: {}".format(max_collision_count))
print("Collisions overall: {}".format(collisions))