
import re
#ignores nodes with / and ? at the beginning
tag_regex = re.compile("<([^?/][^ ><]*) ?.*>")
tag_set = set()
root = 0
with open('input_ex1.txt') as f:
    for line in f:
        tags = tag_regex.search(line)
        if tags:
            for tag in tags.groups():
                # first tag found must be root
                if root == 0:
                    root = tag
                else:
                    tag_set.add(tag)

print(root)
print() #newline
for tag in tag_set:
    print(tag)
print()
print("Found altogether {} different nodes other than root node.".format(len(tag_set)))