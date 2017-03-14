#!/usr/bin/env python
#How many total hours of airtime did each carrier have?
#Student: Changle Xu, Yuan Gao, Bei Xia

from operator import itemgetter
import sys

current_carrier = ""
carrier = ""
total = 0
airtime = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    count = line.split('\t')

    #Input of the reduce: the key is the carrier. The value is the airtime for that carrier in one instance.
    carrier = count[0]

    airtime = float(count[1])

    if current_carrier == carrier:
        total += airtime
    else:
        #Output of reduce: the key is carrier; the value is the total hours of airtimes that that carrier has. 
        if not total == 0:
                print "Carrier: %s\t" % carrier + "Airtime: %.2f\t" % (float(total)/60)
        current_carrier = carrier
        total += airtime
~                                 
