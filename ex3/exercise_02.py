
# TODO: parse xml, throw exception if invalid
import re
docs = ['input_ex2_1.txt', 'input_ex2_2.txt', 'input_ex2_3.txt']


# Idea: keep a stack of tags, check if they are closed in correct order
# Idea: check if there are only allowed characters in tag
def test_docs_regex(docs):
    tag_regex = re.compile("<([^?][^ ><]*) ?.*?>")
    tag_stack = []
    for doc in docs:
        with open(doc) as f:
            try:
                was_empty = False
                for line_count, line in enumerate(f):
                    tags = tag_regex.findall(line)
                    for tag in tags:
                        if '/' == tag[0]: # ending tag
                            start_tag = tag_stack.pop()
                            was_empty = len(tag_stack) == 0
                            if start_tag != tag[1:]:
                                raise Exception("Problem on line {}, did expect end tag for {}," \
                                      "bug found end tag {}".format(line_count, start_tag, tag[1:]))
                        else:
                            if was_empty:
                                raise Exception("Document does not seem to have a root node, since "
                                                "on line {} there was nothing on stack".format(line_count))
                            tag_stack.append(tag)
                print("{}: YES".format(doc))
            except Exception as e:
                print("{}: NO, {}".format(doc, e))

test_docs_regex(docs)
print()

# Idea: don't do this exercise and just use an xml parser, since there are already way too many of these to write a new one.
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
