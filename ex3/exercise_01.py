
import re
tag_regex = re.compile("</?([^ ><]*) ?.*>")
tag_set = set()
with open('input_ex1.txt') as f:
    for line in f:
        tags = tag_regex.search(line)
        if tags:
            for tag in tags.groups():
                tag_set.add(tag)

print(tag_set)
print(len(tag_set))