#!/usr/bin/python

# This mapper handles stdin text data from forum_node.tsv and outputs,
#   Key: keyword, the lower case keyword, and
# Value: The post id, word order, location catagory.
# Output format:
# author_id \t post_id, word_order, location_catagory

# This mapper generates a text stream with a tab separated index containing the keyword 
# followed by tab seperated word location groups. 
# The word location group contains post_id, word order and location category identify where the keyword can be found.

# * "keyword": The searchable keyword
# * "post_id: The id of the forum post
# * "word_order": the word location in the text, eg. 0 indicates that it's the first word in the text, 12 indicates that it's the 13th word in the text.
# * "location_catagory": indicates if the word is in the body "B", tagnames "T" or the title "H"

# Output
# * keyword \t post_id, word_order, location_catagory

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19:
        continue    # If the 19 columns aren't read, then ignore.
    node_id = line[0]
    if node_id == 'id':
        continue
    body_text = line[4]
    tag_text = line[2]
    title_text = line[1]
    word_list = re.findall("[\w]+", body_text)     # Split body text to extract words, excludes punctuation
    tag_list = tag_text.split()                    # Split tagnames on space, punctuation included
    title_list = re.findall("[\w]+", title_text)   # Split title text to extract words, excludes punctuation
    # List body_text words as key with  node_id, word order, category {B = body_text, T = tagnames, H = title (Heading)} 
    for word_order, word in enumerate(word_list):
        print word.strip().lower(), "\t", node_id, ",", str(word_order), ", B"
    for word_order, word in enumerate(tag_list):
        print word.strip().lower(), "\t", node_id, ",", str(word_order), ", T"
    for word_order, word in enumerate(title_list):
        print word.strip().lower(), "\t", node_id, ",", str(word_order), ", H"
        




