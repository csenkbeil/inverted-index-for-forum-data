#!/usr/bin/python

import sys

wordLocationList = []
oldWord = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisWord, thisWordLocation = data_mapped

    if oldWord and oldWord != thisWord:
        print oldWord, "\t",  " ".join(wordLocationList)
        oldWord = thisWord;
        wordLocationList = []

    oldWord = thisWord
    wordLocationList.append(thisWordLocation)

if oldWord != None:
    print oldWord, "\t", "\t".join(wordLocationList)

