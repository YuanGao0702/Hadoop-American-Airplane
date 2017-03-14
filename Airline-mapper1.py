#!/usr/bin/env python
#Student: Changle Xu, Yuan Gao, Bei Xia
#What is the percentage departures later than 5 minutes from every airport?

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split('","')
    id = words[2]
    crs = words[6]
    dep = words[7]

    if dep.strip():
        crs = int(crs)/100*60+int(crs)%100
        dep = int(dep)/100*60+int(dep)%100
        delay = dep-crs

        #Output of the mapper: the ORIGIN_CITY_NAME is the key; the delay is the value, whose value is 1 or 0.
        if delay>5:
                print '%s\t' % id+ '""' + " 1"
        else:
                print '%s\t' % id+ '""' + " 0"
~                                                                                           
