
import re
docs = ['input_ex2_1.txt', 'input_ex2_2.txt', 'input_ex2_3.txt', 'input_ex2_4.txt', 'input_ex2_5.txt', 'input_ex2_6.txt']

# Tests with regex if xml is valid
def test_docs_regex(docs):
    tag_regex = re.compile("<([^?][^ ><]*) ?.*?>")

    for doc in docs:
        with open(doc) as f:
            try:
                tag_stack = []
                was_empty = False
                for line_count, line in enumerate(f):
                    # fix enumerate to 1 based counting
                    line_count += 1
                    attributes = re.search("<.*?=(.*?)\??>", line)
                    if attributes:
                        for attribute in attributes.groups():
                            if not (attribute[0] == '"' and attribute[-1] == '"'):
                                raise Exception("Attribute {} was not in quotation marks on line {}".format(attribute, line_count))

                    tags = tag_regex.findall(line)
                    for tag in tags:
                        if '/' == tag[0]: # ending tag
                            start_tag = tag_stack.pop()
                            was_empty = len(tag_stack) == 0
                            if start_tag != tag[1:]:
                                raise Exception("Problem on line {}, did expect end tag for {}, "
                                                "but never found one".format(line_count, start_tag, tag[1:]))
                        else:           # starting tag
                            if was_empty:
                                raise Exception("Document does not seem to have a root node, since "
                                                "on line {} there was nothing on stack".format(line_count))
                            if re.search(r'[.,:;]', tag): # could check for mor invalid characters
                                raise Exception('There is an invalid xml tag on line {}: {}'.format(line_count, tag))
                            tag_stack.append(tag)
                if not len(tag_stack) == 0:
                    raise Exception("There were tags that were never closed, namely: {}".format(tag_stack))
                print("{}: YES".format(doc))
            except Exception as e:
                print("{}: NO, {}".format(doc, e))


test_docs_regex(docs)
print()

# Just use an xml parser, since there are already way too many of these to write a new one.
import xml.etree.ElementTree as ET
def test_docs_et(docs):
    for doc in docs:
        with open(doc) as f:
            try:
                t = ET.parse(f)
                print("{}: YES".format(doc))
            except Exception as e:
                print("{}: NO, {}".format(doc, e))

test_docs_et(docs)
