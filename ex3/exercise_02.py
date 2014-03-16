
# TODO: parse xml, throw exception if invalid
import re
docs = ['input_ex2_1.txt', 'input_ex2_2.txt', 'input_ex2_3.txt']


# Idea: keep a stack of tags, check if they are closed in correct order
# Idea: check if there are only allowed characters in tag




# Idea: don't do this exercise and just use an xml parser, since there are already way too many of these to write a new one.
import xml.etree.ElementTree as ET

for doc in docs:
    with open(doc) as f:
        try:
            t = ET.parse(f)
            print("{}: YES".format(doc))
        except Exception as e:
            print("{}: NO, {}".format(doc, e))