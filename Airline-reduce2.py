#!/usr/bin/env python
#How many minutes total did passengers spend waiting for all late departures in 2014?
#Student: Changle Xu, Yuan Gao, Bei Xia

from operator import itemgetter
import sys

total = 0
delay = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    #Input: the key is FL_NUM; the value is the delay whose value is larger than 0 minutes. 
    # parse the input we got from mapper.py
    count = line.split('\t')


    delay = int(count[1])

    total += delay

#There is no key of output of reducer.The value is the total minutes passengers spent waiting for all late departures in 2014.
print "Total Waiting time: "+'%s\t' % (total)
