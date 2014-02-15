#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) != 19:
        continue
    node_id = line[0]
    if node_id == 'id':
        continue
    body_text = line[4]
    tag_text = line[2]
    title_text = line[1]
    word_list = re.findall("[\w]+", body_text)
    tag_list = tag_text.split()
    title_list = re.findall("[\w]+", title_text)
    # List body_text words as key with  node_id, word order, category {B = body_text, T = tagnames, H = title (Heading)} 
    for word_order, word in enumerate(word_list):
        print word.lower(), "\t", node_id, ",", str(word_order), ", B"
    for word_order, word in enumerate(tag_list):
        print word.lower(), "\t", node_id, ",", str(word_order), ", T"
    for word_order, word in enumerate(title_list):
        print word.lower(), "\t", node_id, ",", str(word_order), ", H"
        




