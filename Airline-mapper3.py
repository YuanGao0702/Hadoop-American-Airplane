#!/usr/bin/env python
#How many total hours of airtime did each carrier have?
#Student: Changle Xu, Yuan Gao, Bei Xia

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(',')
    word = words[1].split('"')
    carrier = word[1]
    airtime = words[14]

    #Output of the mapper: the key is the carrier. The value is the airtime for that carrier in one instance.
    if airtime.strip():
        print '%s\t' % carrier + '%s\t' % airtime
~                                                               
