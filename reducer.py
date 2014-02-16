#!/usr/bin/python

# This reducer handles stdin text data generated after the mapper data is sorted and outputs,
#   Key: keyword, the lower case keyword, and
# Value: The post id, word order, location catagory.
# Output format:
# author_id \t post_id, word_order, location_catagory

# This reducer generates a text stream with a tab separated index containing the keyword 
# followed by tab seperated word location groups. 
# The word location group contains post_id, word order and location category identify where the keyword can be found.

# * "keyword": The searchable keyword
# * "post_id: The id of the forum post
# * "word_order": the word location in the text, eg. 0 indicates that it's the first word in the text, 12 indicates that it's the 13th word in the text.
# * "location_catagory": indicates if the word is in the body "B", tagnames "T" or the title "H"

# Output

# * keyword \t post_id, word_order, location_catagory

import sys

wordLocationList = []
oldWord = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord = data_mapped[0]
    thisWordLocation = data_mapped[1]             # Column 2 contains word location group for the keyword
    if oldWord and oldWord != thisWord:
        print oldWord, "\t",  "\t".join(wordLocationList)
        oldWord = thisWord;
        wordLocationList = []

    oldWord = thisWord
    wordLocationList.append(thisWordLocation.strip())   # Append Word location group to WordLocationList

if oldWord != None:
    print oldWord, "\t", "\t".join(wordLocationList)   # Added Word location groups as tab separated items after the keyword

